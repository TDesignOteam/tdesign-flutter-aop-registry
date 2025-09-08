## AOPRegistry 1.1.4
1. 兼容Flutter 3.35及以上版本使用

## flutterPatch 1.1.3
1. 兼容Flutter 3.35及以上版本使用
2. 从flutter3.13版本开始，支持解析dart dev版本

## AOPRegistry 1.1.3
1. 兼容Flutter3.32及以上版本使用

## AOPRegistry 1.1.2
1. 兼容Flutter3.29及以上版本使用

## AOPRegistry 1.1.1
1. 兼容Flutter3.27及以上版本使用

## flutterPatch 1.1.2
1. 兼容Flutter 3.24及以上版本使用

## flutterPatch 1.1.1
1. 修正frontendServerEntry配置，在Flutter 3.3.0上存在引用冲突

## AOPRegistry 1.1.0
1. 增加transformersAfterModular插桩时机，此时可以加入外部引入的语法树节点。

## flutterPatch 1.1.0
1. 修正Flutter 3.19.0+ 版本，web-debug、android/iOS编译问题。无需再回退SDK使用。
2. 修正异常时提示文案，描述更精准。
3. 修正AOPRegistry自动更新可能存在异常，Git运行始终不报错等问题

## flutterPatch 1.0.9
1. 增加Flutter 3.19.0_infinity.patch对FlutterSDK补丁。
2. Dart依赖解析增加third/pkg文件夹遍历，解决Flutter 3.19.0+版本pub get异常。
3. 在Flutter 3.19.0+版本 web-debug、android/iOS，受frontend_server_aot.dart.snapshot影响，需revertSDK 1a44710d19809134fac64ab3fc3cf112e48b0868后使用。

## AOPRegistry 1.0.3
1. 排除dart_style依赖，其在flutter 3.10版本存在错误的commit

## AOPRegistry 1.0.2   flutterPatch 1.0.8
1. 适配Flutter 3.16版本

## AOPRegistry 1.0.1
1. 适配Flutter 3.13版本

## flutterPatch 1.0.7
1. 避免直接删除.git/index.lock

## flutterPatch 1.0.6
1. 修正Git报错时将打印提示
2. 加入获取dart工程失败时的重试逻辑

## flutterPatch 1.0.5
1. 修复Flutter 3.3以上版本，Debug下增量编译，由于再次编译AOP工程导致的错误。

## flutterPatch 1.0.4
1. 修正AOP工程配置相对路径依赖时，pub报错的问题
2. 优化错误提示

## flutterPatch 1.0.3
1. 修正由于url编码，导致引用pub仓库的AOP插件可能报错的问题。

## flutterPatch 1.0.2
1. 修正切换Flutter版本，首次可能pub失败的问题。

## flutterPatch 1.0.1
1. 修正切换工程后，pub get/upgrade可能爆出依赖冲突的问题
2. 修正插件使用时新配置AOP目录，不新改包名就不生效的问题
3. 新增flutterRoot配置，支持本地调试引擎

## AOPRegistry 1.0.0 （稳定版，请使用最新1.+版本的patch）
1. 破坏性更新，增加isInteractiveRecompilation字段，web-dev-run等情景为true。
2. 废弃platform配置，改为compileTarget。参数为frontend_server和dart2js。
3. 增加AOPRegistry依赖异常时retry逻辑，处理Flutter切换后可能的异常。

## flutterPatch 0.0.9
1. 优化pub耗时，重复耗时从10s->5s左右。
2. 默认不在AOP工程的yaml中保存dart依赖。
3. 增加saveDartDependencies，用于主项目AOP工程的dart依赖在yaml保留。（移除recoverYaml配置）
4. 增加setPluginEnable配置，用于强制启用、关闭插件的AOP能力。
5. compile时增加关联AOP工程的校验，改变时自动先pub get。

## flutterPatch 0.0.8
1. 过滤recompile，web编译时的无效调试信息。

## flutterPatch 0.0.7
1. 修正插件AOP工程，无法正常获取的异常。
2. 修正插件AOP工程，dependency_overrides，dev_dependencies缺失依赖传递。
3. 当多个AOP工程使用时，增加可能的依赖冲突提示。
4. 优化dart升级后，自动更新的策略。

## flutterPatch 0.0.6
1. 修正设置frontendServerEntry、dart2JsEntry入口后，web编译异常
2. 同官方一致，当工程未处理AOP依赖就直接编译时，会自动pub get
3. 支持AOP工程使用dependency_overrides，dev_dependencies，完成这类型依赖的传递处理

## flutterPatch 0.0.5
1. 修正依赖处理时，错误删除了AOP工程中的三方依赖
2. 修正dart依赖处理可能发生错误的问题
3. 优化在工程切换时pub耗时

## flutterPatch 0.0.4
1. 修正由于不可变集合remove导致的异常

## flutterPatch 0.0.3
1. 修正由于依赖路径问题导致的pub失败
2. 修正frontendServerEntry、dart2JsEntry入口配置的层级错误

## flutterPatch 0.0.2
1. 修正主工程引用的AOP工程未处理依赖的问题

## 0.0.1
1. 完成AOPRegistry，Flutter AOP统一的集成框架

* Flutter2.2+全版本兼容
* 项目快速集成
* 支持三方插件使用AOP

