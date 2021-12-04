一，UI自动化线性脚本框架步骤：
步骤1：新建项目，导入selenium模块，新建好各种目录，复制好驱动程序
步骤2：编写测试用例1：登录成功的测试用例
步骤3：编写测试用例2：登录失败的测试用例
步骤4：编写测试用例3：主页面操作测试脚本
步骤5：编写执行层脚本：完成用例构建套件的报告的处理
步骤6：添加配置文件 local_config.ini
步骤7：单独封装浏览器的启动
步骤8：单独封装登录的函数
步骤9：添加log日志
步骤10：使用线性脚本框架，编写UI自动化测试用例，每人完成10条以上脚本


Pageobjects 设计模式基础及应用
Page objects概念：
  Pageobjects 是指UI界面上用于与用户进行交互的对象。
它可以指整个页面，也可以指Page上的某个区域。
Pageobjects是你的测试代码的交互对象，是对实际UI的一种抽象模型化。
通过Pageobjects可以减少重复代码的编写
例如：
    很多页面都有同样的header，footer，navigator等部分
如果对这些进行抽象，只写一次就可以在其他地方通过了

Pageobjects设计模式概念：（把一个页面设计成一个类，页面中的控件作为属性，控件的操作作为方法）
  Pageobjects 模式是selenium的一种测试设计模式，
主要是将每一个页面设计为一个class
其中包含页面中需要测试的元素（按钮，输入框，标题等），
这样在Selenium测试页面中可以通过调用 页面类来获取页面元素，这
样巧妙的避免来当页面元素id或者位置变化时，需要改测试页面代码的情况。
当页面元素id变化时，只需要更改测试页面Class中页面的属性即可
    简单来讲，就是将代码以页面为单位进行组织，针对这个页面上的所有信息，相关操作都放到一个类中
从而具体的测试用例变成简单的调用和验证操作。

备注：
PageObjects 与 Page Objects 是不一样的，
Pageobjects用于特指采用Page Objects进行封装的一种设计模式


PO框架1：PageObjects 设计模式
把一个页面设计成一个类，页面中的控件作为属性，控件的操作作为方法
步骤1： login_page.py 文件的编写
    1、处理好驱动的路径问题，编辑启动浏览器代码
    2、把元素变成具体的元素，加识别方法
    3、完善元素的操作
    4、编写测试脚本
    5、扩展：页面上其他元素也要添加进来，动作也要添加进来
小结：页面= 属性+操作 = 元素+元素操作

步骤2： 巩固PO思想，分离出第二个页面
    main_page.py 文件的编写
思路：
    1、添加元素
    2、添加操作
    3、页面的衔接，把login的driver转给（main）主页面
    4、编写测试脚本


步骤3：添加log模块进来，协助调试脚本
    1、导入学python的时候封装好的日志工具模块
    2、使用日志模块


步骤4： Basepage类封装+元素识别数据分离
    步骤1：在common里面创建base_page.py---> BasePage类
    步骤2：LoginPage类，继承BasePage类
    步骤3：回到BasePage类，封装元素识别
    步骤4：在BasePage类中封装元素操作
    步骤5：在改造login_page页面，在改造之前封装的元素操作方法
    步骤6：子类的driver的处理，继承父类basePage的driver
    步骤7：编写测试代码，测试是否可以成功登录

小结：完成了二个页面的分离
    login_page.py
    main_page.py
    1、都需要driver
    2、都需要识别元素
    3、都会要操作元素：点击，输入等

把所有的页面公共的部分，封装出一个父类：base_page
相同的东西不需要写多次
---------------------------------
Pageobject 模型优化使用

分层的思想：
界面层：界面的布局
控件层：单独验证每个控件的功能
功能层：单个或多个功能组合形成一个功能（登录，提交bug）
业务层：单个或多个功能形成业务  (登录的整个业务)

线性脚本的思想： 按操作去识别元素，风险会比较小
Pageobject模式： 先全部识别元素，再进行操作

当前的问题：实例化对象之后，识别所有的元素，然后再去操作，可能发布元素

--------------------------------
self.username_inputbox = self.driver.find_element(By.XPATH, '//input[@name="account"]')

定位一个元素需要哪些信息：
控件的元素名称：element_name（ username_inputbox ）
元素识别方法：locator_type（ By.XPATH ）
定位信息：locator_value （ '//input[@name="account"]' ）
识别元素超时时间：timeout

元素识别数据分离：
页面只存放元素的识别信息（数据），不用识别元素对象，
由BasePage 根据元素的识别信息去识别对象

补充把日志移动到BasePage类中

---------------------------------------------
为什么要分离： 为了方便维护代码框架
数据与代码分离：
需要的数据有：
    1、元素识别的数据
    2、配置数据（文档的路径、邮件、URl）
    3、测试用例数据


怎么去分离数据：放Excel表，mysql，yaml元素数据源设计

思路：
步骤1：创建一个element_info_datas文件夹，把元素识别数据分离出来放Excel表
步骤2：读取Excel表里面的元素识别数据
步骤3：把读取Excel的操作封装成 element_data_unitls.py 模版
步骤4：改造login_page页面，偶从Excel读取元素识别的数据
步骤5：为了避免编写Excel错误，把元素识别的方法做成下拉的方式


config 配置文件的二次封装
步骤1：新建一个config文件夹--> 新建config.ini配置文件 ,并输入数据
步骤2：新建一个config_utils.py 文件,创建类：ConfigUtils
步骤3：新建一个Browser 浏览器驱动类，并封装一个get_chrome_driver()方法
步骤4：替换LoginPage里面的驱动，测试一下
步骤5：处理google浏览器黄色条条的问题
步骤6：在配置文件中添加默认浏览器的类型
步骤7：封装火狐的驱动、封装edge浏览的驱动，把3个获取驱动的方法再次封装成总的获取驱动
步骤8：把不用的驱动方法封装成私有的方法，避免误操作
步骤9：扩展：封装一个分布式的驱动，远程的驱动driver
小结： config二次封装、driver二次封装操作目标

PO框架10：大型业务自动化页面的处理
痛苦点： 一个页面元素的数据放在excel表的一个sheet里面，如果有
100个页面，放100个sheet，不方便操作

思想：
1、三层架构：项目---模块---页面，一个excel的sheet存放一个模块的所有的页面的信息
2、


PO框架11： 页面元素信息分离优化
实战一： 页面元素分离优化
    处理方法1： 新建一个模块的文件夹，然后一个excel表，放在文件夹里面
    处理方法2： 一个模块的所有也是放Excel一个页签里面，加一个所属页面，用例存放当前页面的数据

步骤1：修改Excel表
步骤2：完善element_data_unitls.py
步骤3：

实战二： 对于动态变大的列表---根据独一无二且有业务含义的属性去识别其中一个


PO 框架12： 元素操作封装1： 切框架、js的处理、等待
时间的处理
思想：PO设计模式  页面 ==  元素+ 操作

父类====BascPage
1、封装类浏览器操作
2、元素识别操作
3、元素操作封装  自动化特殊场景的处理

元素的处理
页面类中的元素--- 元素识别操作---元素的数据整理成字典---元素信息转存到excel 表里面

实战1： 在BasePage类中添加切框架操作

PO框架13： 元素操作封装1：等待时间的封装默认等待时间的处理、 Excel表中未填时间的处理
实战1：
1、sleep():固定休眠时间设置
2、implicitlyWait()方法比sleep()方法智能，sleep()方法只能在一个固定的时间等待
    而implicitlyWait()可以在一个时间范围内等待，称为隐式等待
3、WebDriverWait():显示等待，语法如下：WebDriverWait(self.driver, locator_timeout)

实战2：

PO框架14： 元素操作封装2： 鼠标键盘、弹出框的处理

PO框架15： 元素操作封装3：切换句柄的封装、截图封装
实战1： 切换句柄的封装
步骤1：前置工作，在BasePage 中封装获取url 的方法
步骤2：获取当前页面的句柄
步骤3：通过句柄来切页面
步骤4；通过title来判断切句柄
步骤5：通过url网址的判定来切页面
步骤6：继续优化，切的时间加等待时间

实战2：截图的封装
执行测试异常，截图保留现场
步骤1：新建一个界面的文件夹，screen_shop
步骤2：将截图的文件夹添加到配置文件中
步骤3：将ConfigUtils 类中添加获取截图位置的方法
步骤4：在BasePage基本页面类中封装截图的方法

分层：
    数据层--元素层--业务层（功能层）--用例层--执行层
        框架底层：common


步骤零：业务层的编写

步骤一： 在框架底层BascPage里面封装在提示框中默认点击确认，然后返回提示框内容的方法
登录失败，返回提示框的内容

步骤二： 在元素层，LoginPage 封装登录失败返回提示信息的方法

步骤三： 在业务层中，封装登录失败的业务

默认登录业务的处理



1、用例层的编写
Browser--> BasePage--> LoginAction-->LoginCase
步骤1：新建testcases --> 子套件 --> 测试py模块--> test打头的测试方法
步骤2：前置工作：在base_page.py 添加退出关闭浏览器

步骤5：重新封装 main_page.py 页面
前置条件，准备Excel元素信息数据
Browser--> BasePage--> LoginAction-->LoginCase


步骤6： main_page 页面重新封装
前置
步骤7：检查业务层里面的登录操作


unittest 测试框架二次优化
当前遇到的问题
1、setup是否可以统一封装
2、tearDown是否统一调用
3、测试用例中的测试数据的分离

思路：需要封装测试用例基础类： 
selenium_basc_case.py中封装：SeleniumBascCase 类
步骤1： 
setUPClass()  tearDownClass()  setUp()   tearDown()

步骤2：
common--> selenium_basc_case.py 中封装 SeleniumBaseCase() 类继续 unittest.TestCase

步骤3：
改 login_case.py 让所有测试用例继承 SeleniumBaseCase()

步骤4：
个性化设置，

扩展5：EleniumBascCase() 加错误截图


注释讲解_底层封装、业务封装 ExcelUtils 举例

问题1：
    1、代码没有注释，久了不知道自己写了什么东西

注释讲解
知识点1：
 行注释， 块注释
 在代码的关键部分（或比较复杂的地方）



底层封装、业务封装 ExcelUtils 举例
什么是框架底层： 
把框架数据层，页面层，功能层，用例层等需要的一些公共的操作放入框架底层

xlrd --> ExcelUtils类 ---> ElementDateUrils 类


日志的重新封装——日志级别- 底层添加日志

思路：
1、提前准备好封装好的日志
2、步骤1：配置文件添加log_path
3、步骤2：在config_untils() 添加提取log_path
4、添加日志级别，并测试
5、测试通过日志级别控制日志
6、执行测试用例，查看日志
7、给底层模块添加日志：浏览器的驱动类，基本页面类，测试用例类添加日志


运行的脚本异常：要手工确认区别是本身框架的问题，还是系统的bug问题

小结：自动化运行异常的日志及截图
思路：
步骤1： 让元素识别信息Excel表中的定位信息写错

步骤2：添加异常日志：元素识别异常处理及日志

步骤3：系统自动的断言错误，把元素识别改为正确
    手工登录系统输入错误的用户名和密码，让系统的提示信息变一下，让 unittest 断言报错

问题出来了： 日志里面没有断言失败的日志
步骤4：加元素操作异常的处理：点击元素、文本框输入信息加异常

步骤5：元素识别错误截图

遗留问题： 断言失败的日志的添加，断言失败的截图

测试数据的分离：
步骤1： 测试用例的分析，测试用例核心的组成
测试编号，测试用例名称，测试优先级，测试操作步骤，测试数据，预期结果
步骤2：Excel表测试用例设计
步骤3：添加测试用例位置到配置文件中
步骤4： 使用excel_until.py 测试读取测试用例
步骤5：创建一个tets_data_utils.py文件，新建TestDataUtils类，用例读取测试用例数据
测试用例字段设计：
test_login_success {'test_name': '验证是否能成功进行登录', 'isnot': '是', 'excepted_result': '测试人员2', 'test_parameter': {'username': 'test02', 'password': 'newdream123'}}
步骤6： 改造loginCase类，通过 Excel 表中导入测试数据
步骤7：执行LoginCase 测试用例，查看结果


测试报表设计及优化
步骤1： 新建一个存放报告的文件夹
步骤2：将报表的文件夹、测试用例的路径添加到配置文件中
步骤3：导入HTMLTestReportCN.py 模块导common
步骤4：新建一个runner包，然后在这里新建 run_all_cases.py 文件，编写执行脚本
步骤5：执行run_all_cases.py 模块，查看结果
步骤6：元素识别的错误截图，添加到报告中
步骤7：修改元素识别信息，执行用例，查看元素识别失败的截图
步骤8：改测试用例数据，让断言报错，添加断言失败的截图



测试开发：
1、自动化业务工程师  会使用公司现有的框架和平台，编写自动化业务测试用例，会元素识别，元素操作
2、自动化框架工程师  会自己设计编写自动化框架
3、自动化平台架构师  会设计整个自动化平台


控制测试用例是否执行 
思路：
1、需要知道怎么样跳过测试
 如果测试是否执行 如果为 "否" 返回 True   如果为 "是" 返回 Flase
2、修改读取测试用例的工具
3、需要调整用例
4、设置测试数据为类属性，可以给类使用，也可以给对象使用


如果使用当前的框架，在实际工作中，会遇到2个痛苦
1、元素识别文件，只能单人操作，而实际工作中是多人同时操作
2、测试用例数据，多人同时设计测试数据的时候，同时打开数据用例数据的Excel表，
也会存在只能单人操作问题



怎么办？
多人协同优化之一 ....... 元素识别数据
思路：
步骤1： 元素识别文件，按模块为文件夹，页面名为：Excel表名，去掉所属页面列
步骤2：添加配置文件
步骤3：改读取Excel元素的工具类：ElementDataUtils()
步骤4：改页面元素读取文件
步骤5：执行用例执行文件，查看结果


多人协同优化之二
思路：
步骤1： 拆分测试数据
    套件为文件，用例文件名为Excel名
步骤2：改配置文件
步骤3：改 test_data_utils 文件
步骤4：调整测试用例
步骤5：执行测试login_case.py
步骤6：QuitCase 测试类准备测试数据分离
步骤7；执行 run_all_cases.py ,查看日志，邮件、报告


自动化业务工程师---- 元素识别、元素定位   使用公司框架或者平台编写业务测试用例
自动化框架工程师---- 根据公司自己的业务、设计、搭建自己公司的框架
自动化平台架构师---- 设计公司的自动化架构  

