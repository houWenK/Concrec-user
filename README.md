 

 

 

# 基于深度学习的个性化动漫推荐系统

## 1引言

### 1.1编写目的

本手册是基于深度学习的个性化动漫推荐系统最终用户的使用手册，主要为指导用户使用本系统而编写，对本系统的主要功能和操作步骤进行了统一描述和规定。本手册的编写主要以在电脑浏览器端的本系统为例进行详细的介绍说明,其他操作系统在界面上可能有少许差异。

### 1.2背景

#### 1.2.1项目提出的背景

随着互联网技术的不断进步和智能手机的广泛应用，我们如今能够收集到庞大的用户数据。然而，面对网络上海量的信息，人们很难快速有效地获取到自己真正需要的信息，这就导致了信息过载问题的产生。为了解决这个问题，出现了两种主要的方式：搜索引擎和推荐系统。

搜索引擎通过用户输入的关键词来检索相关的结果，虽然这种方式在一定程度上缓解了信息过载问题，但仍然需要用户主动输入关键词，而且结果可能并不完全符合用户的期望。

推荐系统则通过分析用户的历史行为和数据，来预测用户可能感兴趣的内容，并将这些内容推荐给用户。传统的推荐系统通常采用协同过滤算法来实现，但这种算法存在一些明显的局限性，比如冷启动问题和稀疏性问题。

因此，基于深度学习的推荐系统应运而生。这种系统能够学习到更多的用户和物品特征，通过深度神经网络的强大拟合能力，可以更加精准地贴近用户的兴趣，从而实现更加优秀的推荐功能。

本系统旨在设计和实现一个基于深度学习的个性化动漫推荐系统。这个系统可以主动地根据用户的历史观看记录和行为数据，推荐用户可能感兴趣的动漫，以实现对不同用户的个性化推荐。这不仅可以提高用户体验，还可以帮助用户快速发现自己喜欢的动漫，解决信息过载问题。

#### 1.2.2开发的目的

(1) 对平台方而言，流量的高效利用是推荐系统存在的重要原因。 推荐模块不仅使用户在当前页面有了更好的选择路径，同时也给了每个店铺增加入口和展示机会，进而提高了成交概率。

(2) 对信息生产者而言，可以充分挖掘长尾物品，推荐系统的好坏很大程度上决定了平台匹配需求和供给的能力。推荐系统匹配需求和供给的能力决定了其最终的商业价值。

(3) 对信息消费者而言，推荐系统可以让呈现的内容给用户带来惊喜，进而增强用户对平台的依赖。 也会提高平台的转化率。

#### 1.2.3参考资料

[1] Zhang Y,Wang J. A survey on deep learning for recommender systems[J]. Neurocomputing, 2019, 338:1-12. 

[2] 叶长青.一种基于SpringBoot的影视内容推荐系统的设计与实现[J].电脑知识与技术,2023,19(01):85-87.DOI:10.14004/j.cnki.ckt.2023.0015.

[3] 周巧玲. 基于深度学习的琉璃制品推荐系统的设计与实现[D].华东师范大学,2022.DOI:10.27149/d.cnki.ghdsu.2022.004913.

[4] 朱本瑞. 基于Spark的离线与实时的电影推荐系统设计与实现[D].南京信息工程大学,2023.DOI:10.27248/d.cnki.gnjqc.2022.000497.

[5] 杨琳. 基于改进DeepMLP模型的广告点击率预测研究[D].山东大学,2022.DOI:10.27272/d.cnki.gshdu.2022.003856.廖婧,韦攀.物联网技术在智慧校园的应用研究[J].广西广播电视大学学报,2020,31(03):32-36.

[6] 赵辉,袁普及.推荐系统研究[J].科技创新与应用,2023,13(19):97-100.DOI:10.19981/j.CN23-1581/G3.2023.19.0

[7] 岳佩,张浩.基于深度学习的英语教学资源个性化推荐系统[J].信息技术,2023(06):149-153+160.DOI:10.13274/j.cnki.hdzj.2023.06.027.

[8] 张武. 基于召回排序两层模型的特征交互个性化推荐系统研究[D].南京理工大学,2021.DOI:10.27241/d.cnki.gnjgu.2021.002410.

## 2软件概述

### 2.1目的

基于深度学习的个性化动漫推荐系统针对目前动漫推荐系统出现的问题，将满足用户的个性化需求作为创作点，主要为用户设计了动漫搜索查询功能、动漫推荐功能，在数据处理阶段，利用spark对数据进行相应采集，对获取到的数据进行预处理，并将数据存储到MySQL数据库中进行管理。在推荐功能实现阶段，根据召回层和排序层的特点来设计对应模型，通过记录用户的行为，召回层通过deepwalk算法生成用户embedding和动漫embedding，利用局部哈希算法进行快速召回，排序层则采用MLP模型进行预测，以达到更好的满足用户需求的目的。

### 2.2功能概述

结合本软件的开发目的逐项地说明本软件所具有各项功能以及它们的极限范围。它们分别有以下功能：

基于深度学习的个性化动漫推荐系统-用户前台：

(1) 登录，注册

(2) 首页

(3) 动漫查询

(4) 动漫推荐

(5) 动漫相似性推荐

(6) 榜单

(7) 收藏

### 2.3技术选型

后端：Python Flask

前段：vue js css html

数据库：mysql5.7，redis3.2.1

中间件：ElasticSearch7.3.0，spark

### 2.4系统设计

#### 2.4.1系统框架设计

本系统采用PythonFlask框架，falsk框架是一款基于WSGI的轻量级的Web框架,flask犹如耳详的"麻雀虽小,五脏俱全",因此flask具有简单可扩展性的特点。下图是基于深度学习的个性化动漫推荐系统PythonFlask的框架图，图中蓝字为广义上MVC开发模式划分的模块，绿字为Flask框架对应的模块。如图 2.4.1.1所示：

<img src="img/wps1.jpg" alt="img" style="zoom: 33%;" /> 

图2.4.1.1 Python Flask框架图

#### 2.4.2系统架构设计

本系统用ElasticSearch技术进行相关索引的建立，加快查询速度，mysql数据库进行推荐数据的存储。下图是基于深度学习的个性化动漫推荐系统的系统模块架构设计图，反映了系统的工作原理，如图 2.4.2.1 所示：

 <img src="img/wps2.jpg" alt="img" style="zoom:33%;" />

 

图2.4.2.1系统模块架构设计图

#### 2.4.3推荐模块架构设计

本系统推荐模块采用召回->排序->重排的结构，用户通过推荐接口把用户id传入，推荐服务根据用户id在redis中查找用户embedding，召回层通过deepwalk生成用户embedding和动漫embedding并存入redis，通过局部敏感哈希算法进行快速检索筛选动漫，排序层则是把召回层筛选下来的动漫送入训练好的MLP模型，重新评分，然后进行排序，选出TOPn传递给用户。

下图是基于深度学习的个性化动漫推荐系统的推荐模块架构设计图，反映了推荐模块的工作原理，如图 2.4.3.1 所示： 

<img src="img/wps3.jpg" alt="img" style="zoom:33%;" /> 

图2.4.3.1 推荐模块架构设计图

#### 2.4.4召回层的设计与实现

(1) 生成用户观看的动漫行为序列，如图2.4.4.1(a)所示。

(2) 基于用户观看的动漫行为序列构建了物品关系图。可以看出，动漫A和B之间的边产生的原因是用户U1先后观看了动漫A和动漫B。如果后续产生了多条相同的有向边，则有向边的权重被加强。在将所有用户行为序列都转换成动漫关系图中的边之后，全局的动漫关系图就建立起来了，如图2.4.4.1(b)所示。

(3) 采用随机游走的方式随机选择起始点，重新产生动漫序列，如图2.4.4.1(c)所示。

(4) 将这些动漫序列输入到Word2Vec模型中，生成最终的动漫Embedding，如图2.4.4.1(d)所示。

<img src="img/wps4.jpg" alt="img" style="zoom:33%;" /> 

图2.4.4.1 动漫embedding生成过程

#### 2.4.5排序层的设计与实现

本系统采用MLP的深度学习推荐模型，它的优点显著，在两部分联合训练，易部署；结构简单，复杂度低，共享输入，共享信息，可更精确的训练学习。下图是基于深度学习的个性化动漫推荐系统推荐模块中的深度学习模型，如图 2.4.5.1所示：

<img src="img/wps5.jpg" alt="img" style="zoom:33%;" /> 

图2.4.5.1 深度学习推荐模型

### 2.5性能

1.精度

输入数据的精度和本软件输出数据达到的精度得到高质量保证，包括传输中的精度。

2.灵活性

当用户需求(如对操作方式、运行环境、结果精度、时间特性等的要求)发生变化时，本软件的适应能力。

3.安全保密

本软件在安全，保密方面的设计已达到要求。

4.推荐效果

基本实现个性化推荐，用户能得到满意的效果。

### 2.6业务场景

让用户可以通过对应的业务搜索想要的动漫服务，并以深度学习推荐模型的方法给用户做动漫推荐。

### **2.7使用人员**

1、需要获得服务的用户

2、业务的运营人员

## 3开发环境

基于深度学习的个性化动漫推荐系统软件环境是在windows11家庭版下使用python语言进行开发，前端页面展示使用的是 vue框架。数据库使用的mysql8.0版本。开发工具选择PyCharm 2022.2.2和Visual Studio Code进行开发，基础框架采用Flask2.0.3和flask-sqlalchermy2.5.1,中间件采用：ElasticSearch7.3.0，spark。系统硬件环境是在搭载Intel Core i7-12700H(3.5GHz/L3 24M)处理器，内存为32g，显卡为3060ti的笔记本电脑进行开发。

## 4运行环境

### 4.1硬件环境

| 设备名称 | 最低配置                             | 建议配置                             |
| -------- | ------------------------------------ | ------------------------------------ |
| CPU      | Core 15，4核，主频2.5或同等级以上CPU | Core 17，4核，主频3.0或同等级以上CPU |
| 内存     | 4G                                   | 8G                                   |
| 硬盘     | 200G机械硬盘                         | 200G固态硬盘                         |
| 显示器   | 17寸宽屏液晶显示器或以上             | 19寸宽屏液晶显示器或以上             |
| 显卡     | 3060                                 | 3060以上                             |
| 网卡     | 无特别要求                           | 无特别要求                           |

### 4.2软件支持

| 名称              | 版本  |
| ----------------- | ----- |
| Python            | 3.6   |
| Flask             | 2.0.3 |
| flask-sqlalchermy | 2.5.1 |
| mysql             | 5.7   |
| ElasticSearch     | 7.3.0 |
| Redis             | 3.2.1 |

 

## **5系统功能实现**（部分页面）

### **5.1登录**

用户在当前的界面进行相应的账号和密码的设置后，点击界面上的登录按钮进行相应的用户登录操作。如图5.1.1所示。输入正确的应户名和密码即可进入基于深度学习的个性化动漫推荐系统，账号或密码错误则提示对话框“校验失败，用户名或密码错误！”，点击确定，重新进入登录界面，继续登录。登陆后点击头像出现个人菜单，点击退出即可退出系统。如图5.1.2所示。

<img src="img/wps6.jpg" alt="img" style="zoom:33%;" /> 

图5.1.1 登陆模块

<img src="img/wps7.jpg" alt="img" style="zoom:33%;" /> 

图5.1.2 个人菜单模块

### **5.2注册**

用户点击注册即可到注册页面，按照相应要求进行注册，前端会进行相应校验，按要求填完信息后点击确定即可注册成功。如图5.2.1所示。

<img src="img/wps8.jpg" alt="img" style="zoom:33%;" /> 

图5.2.1 注册模块

------

全部资料请私信qq454305202