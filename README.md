# 第一阶段项目 
## 文本冒险游戏 - "神秘的古堡"
这是一个简单的文本冒险游戏，名为“神秘的古堡”。玩家将探索预设的古堡场景，通过输入指令与游戏互动，最终找到逃离古堡的⽅法。
#### 游戏背景故事：
你是⼀名冒险家，迷失在森林中，偶然发现了⼀座神秘的古堡。为了躲避风雨，你推开了古堡虚掩的大门。现在你身处古堡之中，需要找到出口，安全逃离。
#### 游戏流程：
游戏不断循环，等待玩家输⼊指令，处理指令，更新游戏状态，并给出反馈。
- ##### 游戏初始化 
  房间列表（字典建立）：
    
      门厅(Foyer)、大厅(Grand Hall)、走廊(Hallway）、
      图书馆(Library)、餐厅(Dining Room)、厨房(Kitchen)
      【地下通道 - 隐藏出口，需要玩家探索发现，游戏结束，“你成功逃离了古堡！”】
    
  玩家初始位置: 门厅 (Foyer)。
  玩家初始背包：空
 
- ##### 指令处理 handle_input()
   help：显示指令列表 
     
      look : 查看当前房间的详细描述
      go [方向] : 向指定方向移动 (例如: north, south, east, west, down)
      take [物品名称] : 拾取房间内的物品
      inventory : 查看背包中的物品
      quit : 退出游戏
  look：describe_room()
  go [方向]：move()
  take [物品名称]：take()
  inventory：show_inventory()
  quit：sys.exit() 游戏结束，并显示退出游戏的提示信息“感谢游玩！”

- ##### 查看当前房间 describe_room()
  功能:
       
      当玩家输入 look 指令时，游戏详细描述玩家当前所在的房间。
      周围有什么，以及可以往哪些方向移动。

- ##### 移动到其他房间 move()
  功能: 
      
      当玩家输入 go 指令并指定方向时，
      如果该方向有出口:
        将玩家的当前位置更新为⽬标房间，并显示新房间的描述
      如果该方向没有出口:
        给出提示信息"那边没有路"


- ##### 拾取物品 take()
   功能: 
   
      当玩家输入 take 指令并指定物品名称时，拾取房间内的指定物品
      如果房间内有该物品:
        将该物品从当前房间的物品列表中移除。
        将该物品添加到玩家的背包列表中。
        给出拾取成功的提示信息"你拿起了 [物品名称]。"
      如果房间内没有该物品:
        给出提示信息"这⾥没有 [物品名称]" 

- #####  show_inventory()指令： 查看背包
  功能: 
  
      当玩家输入 inventory 指令时，游戏显示玩家当前背包中的物品列表。


