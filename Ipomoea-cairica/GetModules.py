import pcbnew

# pcbnewの配置されている部品一覧を生成する

modules = []

for module in pcbnew.GetBoard().GetModules():
    pos = pcbnew.ToMM(module.GetPosition())
    modules.append(str(module.GetReference()) + ':' + str(pos) + ',' + str(module.GetOrientation() / 10))

modules.sort()

for module in modules:
    print(module)
