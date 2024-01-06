# SI140A-project
Reverse engineering mechanism of Wechat envelope -- SI140A final project for 2023 Fall

Processes:
1. Gathering data of 5 people, 10 people, 20 people as training set and validation set.
2. Find the corresponding model and compare with their loss
3. Use the predicted model to stimulate large amount of actions and compare with validation set.
4. Find the result and work with the bonus.

Timeline:
1. 数据采集+整理 （12/29 - 1/3）
- 5个人 100组（20*5）20块 按顺序
- 10个人 10组 2.5块
- 20个人 5组 5块
- 其中5*85用于“寻找”model；5*15，10*10，20*5用于Justification
- 5*85中有10组在1.1测试（测试节日是否不同）
- 最终数据用excel整理

2. 建模（1/3 - 1/7）
- 公式已有，处理所收集数据
- 寻找是否有其他分布方式或随机算法
- 根据loss function寻找最优公式（即网上所给）

3. Reproduce（1/8 - 1/11）
- 根据得到的公式模拟大量红包，获得模拟数据及其分布

4. Justification （1/12 - 1/14）
- 和（1）中的Justification的数据集进行对比， 获得信息和结论，验证数据集的正确性，给出抢红包的最优解

5. 其他优化（1/15 - 1/20）
- 思考红包接龙的最优解
- user-specific mechanism
- fairness-ware
- 跟红包总金额、红包总数量的相关性

6. ddl为1/21