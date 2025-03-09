import sys
rooms = {
    "门厅": {
        "name": "门厅",
        "description": "-你身处古堡的阴暗门厅。头顶一盏布满蜘蛛网的吊灯微微摇晃，投下忽明忽暗的光芒。空气中弥漫着潮湿的霉味，脚下是冰冷的大理石地面。北面是一扇沉重的橡木门，门上雕刻着狰狞的怪兽头像，东面则是一条通向黑暗深处的走廊。",
        "items": [{"name": "门厅地毯下的纸条", "description": "一张陈旧的纸条，似乎是从某本书页上撕下来的，上面潦草地写着‘光芒指引方向’。"}],
        "exits": {"north": "大厅", "east": "走廊"}
    },
    "大厅": {
        "name": "大厅",
        "description": "-你推开橡木门，进入了古堡的宏伟的大厅。尽管岁月流逝，依稀可见昔日的辉煌。一个巨大的水晶吊灯（虽然已经缺了几盏灯泡）仍然悬挂在高耸的天花板上。彩色玻璃窗阻挡了外界的光线，使得大厅内光线昏暗。南面是你进来的门厅，西面是一扇装饰华丽的木门，通往图书馆，东面则是一道拱形石门，通向餐厅。",
        "items": [{"name": "壁炉拨火棍", "description": "一根沉重的铁制拨火棍，顶端装饰着狮子头。"}],
        "exits": {"south": "门厅", "west": "图书馆", "east": "餐厅"}
    },
    "走廊": {
        "name": "走廊",
        "description": "-你沿着昏暗的走廊前行，脚踩在吱吱作响的木地板上。墙壁上挂着褪色的家族画像，画像中的人物表情模糊不清，仿佛在注视着你。走廊尽头似乎传来微弱的滴水声。",
        "items": [{"name": "生锈的铁钥匙", "description": "一把锈迹斑斑的铁钥匙，看起来年代久远，也许能打开古堡的某扇门。"}],
        "exits": {"west": "门厅"}
    },
    "图书馆": {
        "name": "图书馆",
        "description": "-你推开装饰华丽的木门，走进了布满灰尘的图书馆。高耸的书架一直延伸到天花板，上面堆满了布满灰尘的书籍。空气中弥漫着浓重的旧书和皮革的味道，令人昏昏欲睡。阳光透过高窗洒进来，照亮了书架上零星散落的金箔。",
        "items": [{"name": "一本厚重的古书", "description": "一本皮面精装的古书，书页已经泛黄，封面上用难以辨认的文字写着书名。"}],
        "exits": {"east": "大厅"}
    },
    "餐厅": {
        "name": "餐厅",
        "description": "-你穿过拱形石门，来到了宽敞的餐厅。长长的橡木餐桌上布满了厚厚的灰尘，锈迹斑斑的银质餐具散落在桌面上，仿佛一场盛宴突然中断。墙壁上挂着巨大的狩猎场景油画，画布已经开始剥落。",
        "items": [{"name": "银色烛台", "description": "一个精致的银色烛台，上面镶嵌着一些宝石，但大部分已经脱落。"}],
        "exits": {"west": "大厅", "north": "厨房"}
    },
    "厨房": {
        "name": "厨房",
        "description": "-你推开破旧的木门，进入了阴冷潮湿的厨房。腐烂的气味扑鼻而来，令人作呕。生锈的厨具散落在各处，巨大的壁炉已经冰冷，炉膛里堆满了黑色的灰烬。地板中央有一块不寻常的木板。",
        "items": [
            {"name": "火柴", "description": "一盒潮湿的火柴，看起来还能用。"},
            {"name": "水桶", "description": "一个破旧的木水桶，里面积满了浑浊的雨水。"}
        ],
        "exits": {"south": "餐厅", "down": "地下通道"}
    }
}

current_room = rooms["门厅"]
inventory = []
game_active = True

def handle_input(command):
    if command == "help":
        print("可用指令:","help - 显示帮助信息","look - 查看当前房间",
         "go [方向] - 向指定方向移动 (north, south, east, west, down)",
         "take [物品名称] - 拾取物品","inventory - 查看背包","quit - 退出游戏",sep='\n')
    elif command == "look":
        describe_room()
    elif command.startswith("go "):
        direction = command.split(" ")[1]
        move(direction)
    elif command.startswith("take "):
        item_name = command.split(" ", 1)[1]
        take(item_name)
    elif command == "inventory":
        show_inventory()
    elif command in ("quit", "exit"):
        print("感谢游玩！再见！")
        sys.exit()
    else:
        print("无效指令，请输入 help 查看可用指令。")

def describe_room():
    print(f"你身处{current_room['name']}:")
    print(current_room['description'])  
    if current_room['items']:
        print("\n房间里有：")
        for item in current_room['items']:
            print(f"- {item['name']}:{item['description']}")
    else:
        print("\n房间里没有明显的物品。")  
    if current_room['exits']:
        print("\n你可以向以下方向移动：")
        for direction, target in current_room['exits'].items():
            print(f"- {direction}({target})")
    else:
        print("\n没有明显的出口。")

def move(direction):
    global current_room, game_active
    if direction in current_room['exits']:
        target = current_room['exits'][direction]
        if target == "地下通道":  # 逃脱成功条件
            print("你掀开地板上的活板门，顺着梯子爬了下去...")
            print("你成功逃离了古堡！")
            game_active = False
        else:
            current_room = rooms[target]
            describe_room()
    else:
        print("那边没有路。")

def take(item_name):
    for item in current_room['items']:
        if item['name'] == item_name:
            inventory.append(item)
            current_room['items'].remove(item)
            print(f"你拿起了 {item_name}。")
            return
    print(f"这里没有 {item_name}。")

def show_inventory():
    if inventory:
        print("你的背包里有：")
        for item in inventory:
            print(f"- {item['name']}:{item['description']}")
    else:
        print("你的背包是空的。")

print("(输入 help 查看指令)\n")
print("游戏背景：你是一名冒险家，迷失在森林中，偶然发现了一座神秘的古堡。为了躲避风雨，你推开了古堡虚掩的大门。现在你身处古堡之中，需要找到出口，安全逃离。\n")
describe_room()

while game_active:
    command = input("\n> ").strip().lower()
    handle_input(command)
    