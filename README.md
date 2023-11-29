# 罗德岛物价局
## 功能
根据自定义价值观基础计算精英材料价值，并参照定价对各种商店的购买性价比进行比较和排序。

## 面对的问题
《明日方舟》中的精英材料价值，在目前的主流学说中是依附于目前的这上千关卡而决定的，而关卡掉落各种材料的掉率被认为是在较长时间范围内趋于恒定的，这些关卡的材料的掉落期望反映了材料价值之间的线性相关关系。

而各位博士手中可以用于兑换各类材料的货币不只有理智一种，为了了解用什么货币去兑换什么材料最为合算，通过这些关卡去确定精英材料的理智价值，并与其他货币进行比较，再按照货币兑换的性价比指导兑换行为就是是一套容易想到的解决方案。

## 算法简述
上千关卡的约束条件对应几十种材料价值作为未知数，其中大多关卡带来的条件会成为松约束，那么如何筛选参与定价的关卡就是问题本质所在了。

本项目迭代选择与待定价材料相等数量的定价关卡，解一次方程组就得到了材料的定价，判断筛选范围内的关卡是否服从定价：不服从的关卡替代现有定价关卡成为新的定价关卡并重新进行方程组求解；而所有关卡都服从定价时就确定了最终的材料定价。
再通过定价结果计算各商店的兑换货币性价比，从而指导“在什么商店买什么”的问题。

总体算法大抵如上所述，但是算法中涉及的各项参数其实应该是按照实际情况进行设置的。

但是众所周知，价值观是因人而异的，即使在游戏中也是如此。
这受各位玩家的经济能力、心态玩法以及认识水平影响，影响着甚至可以说是决定了每名博士所面对的“实际情况”。
因此在计算之前就应该按照博士自身的情况指定一套价值观，然后再开始计算。
当然，对于选择困难的博士，该项目也准备了一套后期符合一般玩家经济水平、折算理智最优策略的价值观作为默认输入，供大家参考。

## 页面截图
![image](https://github.com/Bidgecfah/-/assets/112526130/02668712-eea8-45c1-96d1-a66805f9c452)
![image](https://github.com/Bidgecfah/-/assets/112526130/5919e840-9d17-4bbd-9316-99b15ba259e0)
![image](https://github.com/Bidgecfah/-/assets/112526130/a324956a-9e6d-401e-95a8-9022ec850e5e)
