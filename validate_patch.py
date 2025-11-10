#!/usr/bin/env python3
"""
Patch File Validator for tdesign-flutter-aop-registry

This script validates that the patch files contain the correct code for Flutter compatibility.
"""

import sys
import re
from pathlib import Path


def check_dependencies_type_enum(content: str) -> tuple[bool, str]:
    """Check if DependenciesType enum is properly defined."""
    pattern = r'enum DependenciesType\s*\{[^}]*\}'
    matches = re.findall(pattern, content, re.DOTALL)
    
    if not matches:
        return False, "❌ DependenciesType enum not found"
    
    enum_content = matches[0]
    required_members = ['local', 'git', 'pub', 'all']
    
    for member in required_members:
        if member not in enum_content:
            return False, f"❌ DependenciesType enum missing member: {member}"
    
    return True, "✅ DependenciesType enum correctly defined"


def check_helper_functions(content: str) -> tuple[bool, str]:
    """Check if _normalYaml and _toYamlString functions are defined."""
    normal_yaml_pattern = r'dynamic _normalYaml\(dynamic yamlNode\)'
    to_yaml_string_pattern = r'String _toYamlString\(dynamic yamlData, String indentation'
    
    if not re.search(normal_yaml_pattern, content):
        return False, "❌ _normalYaml function not found"
    
    if not re.search(to_yaml_string_pattern, content):
        return False, "❌ _toYamlString function not found"
    
    return True, "✅ Helper functions (_normalYaml, _toYamlString) correctly defined"


def check_process_decorator(content: str) -> tuple[bool, str]:
    """Check if ProcessDecorator uses nullable Encoding? types."""
    # Check run method
    run_pattern = r'Future<ProcessResult>\s+run\([^)]*Encoding\?\s+stdoutEncoding[^)]*Encoding\?\s+stderrEncoding'
    if not re.search(run_pattern, content, re.DOTALL):
        return False, "❌ ProcessDecorator.run() method doesn't use Encoding? (nullable) types"
    
    # Check runSync method  
    run_sync_pattern = r'ProcessResult\s+runSync\([^)]*Encoding\?\s+stdoutEncoding[^)]*Encoding\?\s+stderrEncoding'
    if not re.search(run_sync_pattern, content, re.DOTALL):
        return False, "❌ ProcessDecorator.runSync() method doesn't use Encoding? (nullable) types"
    
    return True, "✅ ProcessDecorator methods use correct Encoding? (nullable) types"


def validate_patch_file(patch_file_path: str) -> bool:
    """Validate a patch file."""
    path = Path(patch_file_path)
    
    if not path.exists():
        print(f"❌ Error: Patch file not found: {patch_file_path}")
        return False
    
    print(f"\n{'='*70}")
    print(f"Validating: {path.name}")
    print(f"{'='*70}\n")
    
    try:
        content = path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False
    
    checks = [
        ("DependenciesType Enum", check_dependencies_type_enum),
        ("Helper Functions", check_helper_functions),
        ("ProcessDecorator Class", check_process_decorator),
    ]
    
    all_passed = True
    for check_name, check_func in checks:
        passed, message = check_func(content)
        print(f"{check_name:.<50} {message}")
        if not passed:
            all_passed = False
    
    print(f"\n{'='*70}")
    if all_passed:
        print("✅ All checks passed! Patch file is valid for Flutter 3.32.0")
    else:
        print("❌ Some checks failed! Please verify the patch file integrity")
    print(f"{'='*70}\n")
    
    return all_passed


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        patch_files = sys.argv[1:]
    else:
        # Default to checking the 3.24~3.32 patch
        patch_files = ["patch_flutter/3.24~3.32.patch"]
    
    all_valid = True
    for patch_file in patch_files:
        if not validate_patch_file(patch_file):
            all_valid = False
    
    sys.exit(0 if all_valid else 1)


if __name__ == "__main__":
    main()
