#!/bin/bash

# 区别2.14+，未使用空安全
if [[ "$OSTYPE" =~ ^darwin ]]; then
  sed -i "" "s/library fasta.kernel_target;/library fasta.kernel_target; import 'package:vm\/aop.dart';/g" $1
  sed -i "" "s/runBuildTransformations();/runBuildTransformations(); AOPMarket.transformersAfterModular.forEach((transformer) {transformer.transform(component);});/g" $1
  sed -i "" "s/void runBuildTransformations() {/void runBuildTransformations() { AOPMarket.transformers.forEach((transformer) {transformer.transform(component);});/g" $1
  sed -i "" "s/backendTarget.performModularTransformationsOnLibraries(/AOPMarket.transformersBeforeModular.forEach((transformer) {transformer.transform(component);}); backendTarget.performModularTransformationsOnLibraries(/g" $1
else
  sed -i "s/library fasta.kernel_target;/library fasta.kernel_target; import 'package:vm\/aop.dart';/g" $1
  sed -i "s/runBuildTransformations();/runBuildTransformations(); AOPMarket.transformersAfterModular.forEach((transformer) {transformer.transform(component);});/g" $1
  sed -i "s/void runBuildTransformations() {/void runBuildTransformations() { AOPMarket.transformers.forEach((transformer) {transformer.transform(component);});/g" $1
  sed -i "s/backendTarget.performModularTransformationsOnLibraries(/AOPMarket.transformersBeforeModular.forEach((transformer) {transformer.transform(component);}); backendTarget.performModularTransformationsOnLibraries(/g" $1
fi

