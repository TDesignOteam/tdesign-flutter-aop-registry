import 'package:vm/aop.dart';
import 'example/type_transformer.dart';

/// 请在start函数中注册Transformer
///
/// compileTarget
/// * frontend_server: Android/iOS、web-dev-run
/// * dart2js: web profile/release
///
/// isInteractiveRecompilation:
/// * true: web-dev-run，hot-restart...
void start(List<String> args, String compileTarget, bool isInteractiveRecompilation) {
  // 示例代码
  AOPMarket.registerTransformers(TypeTransformer());
}