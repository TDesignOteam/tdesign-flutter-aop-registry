# AOPRegistry 
标准化的Flutter AOP集成框架，支持Flutter全版本，插件开发也可使用的AOP能力。

- [x] 兼容Flutter全版本：有利于业务方处理Flutter快速迭代的现状。

- [x] 支持插件使用：对使用AOP能力的插件提供了普适的集成方式。

- [x] 极简上手：支持Android/iOS/Web，集成方便、调试信息齐全。


## Flutter AOP简介
Flutter AOP是在编译期间在切面角度进行编程，实现收集项目信息、修改代码、全局统一编码策略的方式。

Flutter AOP实现方式是对编译时抽象语法树(AST)进行操作，详见[《Ast语法树操纵》](https://juejin.cn/post/7036352267389239303)
<img width="800"  alt="image" src="https://github.com/user-attachments/assets/b6ed8dcd-9c2f-4d23-98e1-9dcf0fbca4c3" />

## 快速上手
### 1. 标准化集成，向FlutterSDK打入 [「git补丁」](https://github.com/TDesignOteam/tdesign-flutter-aop-registry/tree/main/patch_flutter)。
```
// 在FlutterSDK目录下，请应用对应flutter版本补丁
git apply aop_market/patch_flutter/3.24.0~infinity.patch

// 删除SDK/bin/cache/flutter_tools.stamp，使修改生效。
rm ./bin/cache/flutter_tools.stamp
```

### 2. 业务项目：加入AOP能力
a. 拷贝[example中aop_tools（插桩工程）](https://github.com/TDesignOteam/tdesign-flutter-aop-registry/tree/main/_example/aop_tools)到项目根目录下。

<img width="300" alt="image" src="https://github.com/user-attachments/assets/1ccf4232-0c74-474d-b830-254f047d625b" />

b. 在项目目录（非插桩工程）下执行pub get，完成AOP环境处理。

<img width="800" alt="image" src="https://github.com/user-attachments/assets/fba1d3d3-bbf8-4c5f-a516-56f519e55356" />

c. 在aop_tools的starter.dart中注册修改语法树的Transfomer。

<img width="800" alt="image" src="https://github.com/user-attachments/assets/cc6c2ea1-cdac-44ff-b5d4-0dd4fa4be99d" />

运行项目即可生效AOP逻辑。
<br/>


### 3. 插件开发：加入AOP能力
插件开发者需要关注对Flutter版本的普适性，处理Flutter各版本AST的差异。

a. 同「2」业务项目一致的集成方式
<br/>

b. 修改aop_tools文件夹名，及工程名，避免使用方依赖冲突。建议与插件名关联，可根据Flutter不同版本的AST差异配置多个目录。

<img width="1324" height="182" alt="image" src="https://github.com/user-attachments/assets/644ee70a-bbe2-4cf8-a095-a9b5dceb42d5" />

c. 在插件主目录（非AOP工程目录下）的pubspec.yaml中配置AOP工程位置，并注明不同版本对应的映射关系

```
# pubspec.yaml中配置
AOPRegistry:
  enable: true
  compileTarget: frontend_server, dart2js # 默认android/iOS/web都支持插桩
  
  # [x ~ x)，配置不同Flutter版本对应的AOP工程
  versions:
    1.0.0~2.0.0:
      unsupportTips: Flutter1.+未适配AOP，xx功能不支持
    2.0.0~3.0.0:
      path: ./aop_tools_v2
    3.0.0~infinity:
      path: ./aop_tools_v3
```

当业务项目完成「1」标准化集成的情况下，依赖插件项目，插件项目所携带的AOP逻辑将生效。
<br/>

### 4. 如何调试
编译项目时，将打印调试日志如下

<img width="800" alt="image" src="https://github.com/user-attachments/assets/837aa0db-23cd-44fb-9a16-25058aa9d591" />

建立Dart命令调试行，按日志填入调试信息，即可执行AOP代码的调试。<img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/ee3807a3-49d3-4c9b-9881-c6404cd9ec36" />

<img width="400" alt="image" src="https://github.com/user-attachments/assets/8c1804d2-80c2-4b99-a05b-9e1806bdb21c" />

<img width="800" alt="image" src="https://github.com/user-attachments/assets/d13c6268-b22a-47f4-9e8a-22a6b2777b30" />


## 常见问题
### Q1：为什么会有AOPRegistry?
切面编程是一种常用的编码手段，但在Flutter并没有得到有效的支持。业内能找到的更像是一种应对项目情况的特殊处理：AOP依赖的内容是固定的，对应Flutter版本是固定的。也因此我们在使用多个依赖AOP方案时将遇到难题————它们都有各自的特殊处理，在升级Flutter时也不得不对AOP环境进行适配。

为什么不能一致的方案呢？像Android - gradle transfomer能力一样，提供基础的框架。在统一生态下，让AOP脱离Flutter版本，AOP开发、依赖使用AOP的插件像普通开发一样自然。

### Q2：遇到了不兼容的Flutter版本？
最低支持Flutter 2.2.0，更低未支持主要是考虑到版本太旧、适配非空安全较麻烦。<br/>
最高已验证Flutter 3.29.x，不排除Flutter更新引起AOPRegistry异常的可能，请联系开发团队解决。

所有Flutter版本集成方式是一致的。

### Q3：AOPRegistry可选配置？
除上文提到的配置外，AOPRegistry有一些在主工程pubspec.yaml配置的可选项，用于满足自定义需求，配置后pub get/upgrade生效。

* setPluginEnable：用于强制打开/关闭某个插件的AOP逻辑。
* frontendServerEntry：用于指定编译时frontend_server入口，当需要对编译流程做特殊处理时使用。
* dart2JsEntry：用于指定编译时dart2js入口，当需要对编译流程做特殊处理时使用。

<img width="800" alt="image" src="https://github.com/user-attachments/assets/31d61a50-f299-4313-84f0-c6c5c5d82d44" />

