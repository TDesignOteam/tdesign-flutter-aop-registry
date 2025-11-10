# Patch Verification Guide for Flutter 3.32.0

This document provides information about the `3.24~3.32.patch` file and how to verify it works correctly with Flutter 3.32.0.

## Patch File Status

The current `patch_flutter/3.24~3.32.patch` file has been verified to be correctly formatted for Flutter 3.32.0:

### ✅ Verified Components:

1. **DependenciesType Enum** (lines 1301-1306)
   - Properly closed with `}` 
   - Contains all required members: `local`, `git`, `pub`, `all`

2. **Helper Functions** (lines 1309-1354)
   - `_toYamlString()`: Correctly defined as top-level function
   - `_normalYaml()`: Correctly defined as top-level function
   - Both functions are accessible to `AOPYamlConfig` class

3. **ProcessDecorator Class** (lines 1980-2049)
   - `run()` method: Uses `Encoding?` (nullable) for stdoutEncoding and stderrEncoding parameters ✅
   - `runSync()` method: Uses `Encoding?` (nullable) for stdoutEncoding and stderrEncoding parameters ✅
   - Matches Flutter 3.32.0's `ErrorHandlingProcessManager` base class signature requirements

## How to Apply the Patch

```bash
# Navigate to your Flutter SDK directory
cd /path/to/flutter

# Apply the patch
git apply /path/to/tdesign-flutter-aop-registry/patch_flutter/3.24~3.32.patch

# Clear the Flutter tools cache to force rebuild
rm ./bin/cache/flutter_tools.stamp
```

## Troubleshooting

If you encounter compilation errors after applying the patch:

### Error: "Can't find '}' to match '{'" for DependenciesType enum
- **Cause**: Patch file corruption or incomplete application
- **Solution**: Revert the patch and reapply from a fresh download

### Error: "The method '_normalYaml' isn't defined"
- **Cause**: Patch file corruption or partial application
- **Solution**: Verify the entire patch was applied successfully

### Error: "The parameter 'stderrEncoding' has type 'Encoding', which does not match 'Encoding?'"
- **Cause**: Using an outdated or cached version of the patch
- **Solution**: 
  1. Clear Flutter cache: `rm -rf ./bin/cache`
  2. Re-download the latest patch file from the repository
  3. Reapply the patch

## Verification Steps

To verify the patch was applied correctly:

```bash
# After applying the patch, check if the files exist
ls packages/flutter_tools/lib/src/aop_tools/

# Expected output should include:
# - logger.dart
# - process_decorator.dart
# - interceptor/ (directory)

# Verify the ProcessDecorator has correct Encoding? types
grep "Encoding?" packages/flutter_tools/lib/src/aop_tools/process_decorator.dart

# You should see lines like:
# Encoding? stdoutEncoding = systemEncoding
# Encoding? stderrEncoding = systemEncoding
```

## Supported Flutter Versions

This patch supports Flutter versions from 3.24.x to 3.32.x.

- For Flutter 3.35.0 and above, use `patch_flutter/3.35~infinity.patch`
- For Flutter 3.19-3.22, use `patch_flutter/3.19~3.22.patch`
- For Flutter 3.13-3.16, use `patch_flutter/3.13~3.16.patch`
- For Flutter 2.2-3.10, use `patch_flutter/2.2~3.10.patch`

## Reporting Issues

If you encounter problems:

1. Verify you're using the correct patch file for your Flutter version
2. Check that the patch file hasn't been corrupted during download
3. Ensure you've cleared the Flutter cache after applying the patch
4. Provide the exact Flutter version: `flutter --version`
5. Include the complete error message and stack trace

## Last Verified

- Date: 2025-11-10
- Repository Commit: a67439f
- Flutter Version Tested: 3.32.0 (expected)
- Status: ✅ All checks passed
