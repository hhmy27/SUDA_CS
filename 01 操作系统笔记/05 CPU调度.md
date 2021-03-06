[toc]

# 05 CPU调度

## 测验

![1  0  0  0  犖 选 （ 5 分 ） 由 新 建 状 态 转 换 为 就 緒 状 态 的 调 度 方 式 是 0 ·  A. 长 程 调 度  B. 中 程 调 度  C. 程 淵 度  D 过 呈 淵 度  正 确 答 案 ： A 你 选 为 c ](MdAsset/05 CPU调度/clip_image001.png)



新建到就绪的转换，应该是长程调度，也就是我们说的作业调度/高级调度，下图来自 OS中的调度 补充笔记

![image-20201029200725131](MdAsset/05 CPU调度/image-20201029200725131.png)

![5  O  0  0  单 选 （ 5 分 ） 假 设 一 个 系 统 中 有 4 个 进 程 ． 它 们 到 达 的 时 间 依 次 为 0 、 2 、 4 和 6 ，  运 行 时 间 依 次 为 3 、 4 和 5 。 若 按 照 抢 占 式 短 作 业 优 先 调 度 算 法 调 度 CPU ， 那  么 各 进 程 的 平 均 周 转 时 间 为 0 。  A. 其 它  & 孔 5  C. 6  D. 8  正 答 就 B 你 选 婀 了 ](MdAsset/05 CPU调度/clip_image001-1603973317609.png)

一道经典的题目，建议自己算一下

![( ) 盟 損 , ← 、 ー 出 翌 奝 箞 コ do (Vs) 紐 8  0 残 を V 再 当  -IT 壊 に ・ 0 0  準 ョ イ 0  匯 壊 に ・ 8 0 ](MdAsset/05 CPU调度/clip_image001-1603973328611.png)

新建进程也需要转移到就绪态，并不是一新建就马上能抢占

![10  0  0  0  (5分) MLQ까度算i去喬要考讐」同題中, 不包恬 0 .  A. 每-BA列下」凋度算i宏  8. 迸程升級和降鈒)5}宏  c. BA列數  0. 決定新迸桯霧迸入郄수畎列下」方i宏  正踊答후: B 류Bi瑟力A ](MdAsset/05 CPU调度/clip_image001-1603973368272.png)

MLQ调度算法是多级队列调度算法，不需要考虑进程升降级方法

![12  多 选 （ 5 分 ） 任 时 间 片 轮 转 法 中 ， 时 司 片 、 ， 贝  A. 讲 程 切 频 蘩  B. 平 均 晌 应 时  0 系 统 开 悄 大  D. ． 平 均 等 待 时 种  正 确 答 室 ： A 、  B 、  C 你 选 为 C 、 D ](MdAsset/05 CPU调度/clip_image001-1603973419009.png)

等待时间是指进程等待CPU的时间之和，极端情况下RR算法退化成FCFS算法，此时等待时间一定，当时间片很小的时候会进行多次进程切换导致每个进程等待时间增加，比如说4，4，4本来用FCFS是0，4，8，当时间片为1的时候明显比FCFS长

![13  (55}) .  B. PR  C. SJF  D. FCFS ](MdAsset/05 CPU调度/clip_image001-1603973520563.png)

RR是时间片轮转，PR是优先级调度，SJF是短作业优先，FCFS是先到先服务
PR和SJF都能会产生饥饿

![v 9 卫  0  「 S ( 9 ) ](MdAsset/05 CPU调度/clip_image001-1603973548070.png)

SJF的平均等待时间和平均周转时间最小，并不是响应时间

![9  o  O  O  (59) .  B. SJF  C. FCFS ](MdAsset/05 CPU调度/clip_image001-1603973561026.png)

使用优先级调度算法，可以按照短作业+优先级，FCFS+优先级

## 作业

![1  （ 25 分 ）  有 一 个 操 作 系 统 采 用 多 级 反 馈 队 列 调 度 ， 如 下 图 所 示 的 其 中 第 一 级 采 用 时 间 片 轮 转 算 法 ， 时 间 片  大 小 为 8 “ ， 第 二 级 同 样 采 用 时 间 片 轮 转 算 法 ， 时 间 片 大 小 为 16m 第 三 级 采 用 先 来 先 服 务 算 法 。  根 掘 下 表 给 出 的 5 个 进 程 的 到 达 时 间 、 执 行 时 间 回 答 下 面 的 问 题 。  （ 时 间 以 麾 秒 为 单 位 ）  10  5  达 、 日  0  2  3  4  （ 1)  （ 2 ）  请 画 出 5 个 进 程 执 行 的 甘 特 图 。  根 据 以 上 的 调 度 算 法 ， 分 别 计 算 出 每 个 进 程 的 周 转 时 间 和 响 应 时 间 。 ](MdAsset/05 CPU调度/clip_image001-1603973590273.png)

**答案：**

![image-20201029201324197](MdAsset/05 CPU调度/image-20201029201330885.png)

---

![2  （ 2 什 么 是 抢 占 式 调 度 2 什 么 是 非 抢 占 式 调 度 ？ 各 适 用 什 么 场 合 ？ ](MdAsset/05 CPU调度/clip_image001-1603973618732.png)

**答案：**

- 抢占式调度:
  进程在运行过程中，如果有重要或紧迫的进程到达（其状态必须为就绪），则现运行进程将被迫放弃CPU，系统将CPU分配给新到达的进程
  适合交互式系统 

- 非抢占式调度:
  一旦把CPU分配给某个进程后，系统不可以抢占已分配的CPU给其他进程
  只有进程自愿释放CPU ，才可把CPU分配到其他进程
  适合批处理系统

---

![3  （ 25 分 ）  考 以 下 的 一 个 基 于 优 先 （ 优 先 数 高 优 先 低 ） 的 调 度 算 法 ， 此 算 法 采 用 根 据 等 待 时 间 和 运 行  时 间 对 优 先 数 进 行 动 态 老 化 算 法 ， 具 体 算 法 如 下 ：  a) 处 于 等 待 队 列 中 的 进 程 的 优 先 数 p 根 据 等 待 时 间 t （ 每 毫 秒 计 算 一 次 ） 进 行 变 化 ， p=p-ti  处 于 运 行 状 态 的 进 程 的 优 先 数 p 根 据 运 行 时 间 t （ 每 毫 秒 计 算 一 次 ） 进 行 变 化 ， p=p+t ；  c) 优 先 数 p 每 隔 1 毫 桫 重 新 计 算 ；  d) 采 用 抢 占 式 调 度 筱 略 ：  根 据 下 表 给 出 的 5 个 送 程 的 到 达 时 间 、 执 行 时 间 回 答 下 面 的 问 ·  相 同 时 ， 先 进 入 就 绪 队 列 的 进 程 优 先 ）  0  2  3  4  （ 时 间 以 毫 秒 为 单 位 ， 当 优 先 级  8  4  6  2  10  （ 1)  （ 2 ）  5  6  3  4  2  请 画 出 5 个 进 程 执 行 的 甘 特 图 。  根 据 以 上 的 调 度 算 法 ， 分 别 计 算 出 每 个 进 程 的 周 转 时 间 和 响 应 时 间 。 ](MdAsset/05 CPU调度/clip_image001-1603973679192.png)

这道题很坑，题目想表达的是p=p-1，但给的是p=p-t，参考18年的题目，并且优先级相同的时候就是按照第一次入队的顺序来选择的

老师的回复:

![答 幸 没 有 问 题 ，  优 先 级 是 的 意 思 是 等 待 时 河 t 后 ， 原 来 的 优 先 级 p 变 为 p 一 t.  也 就 是  如 果 1 的 单 位 是 毫 秒 ， 每 过 1 毫 秒 优 先 数 减 1. ](MdAsset/05 CPU调度/clip_image001-1603973686961.png)

答案：

![image-20201029201451963](MdAsset/05 CPU调度/image-20201029201451963.png)

---

![4  （ 10 分 ） 试 上 匕 《 斟 呈 调 与 作 业 调 度 的 不 伺 点 · ](MdAsset/05 CPU调度/clip_image001-1603973703005.png)

**答案：**

从切换频率角度看，进程调度切换频率高，速度快；而作业调度切换频率低，切换慢。因为每个进程在其生命周期中只有一次作业调度，而有很多次进程调度。    从切换开销角度分析，进程调度切换开销小，而作业调度切换开销大。因为作业调度需要把进程的代码和数据从外存调入内存，这些        I/O 操作很耗时。    在多数操作系统中，进程调度是必需的，而作业调度则是可选的。       

---

![考 虑 下 面 基 于 动 态 饶 先 权 可 抢 占 式 调 度 去 ， 大 优 卉 表 示 代 表 高 饶 先 权 · 当 一 个 进 程 旺 等 待  CPU 时 （ 在 就 绪 队 列 中 。 但 耒 仇 行 优 先 数 以 a 速 率 变 化 ； 当 它 运 行 时 ． 优 先 数 以 速 率 阝 变  所 有 进 程 任 进 入 就 绪 队 列 时 被 给 定 优 卉 数 为 0 · 清 司 ：  1 ） 阝 > 0 > 0 时 是 什 么 法 ？ 为 什 么 ？  2 ） a < 阝 < 0 时 是 什 么 去 ？ 为 什 么 ？ ](MdAsset/05 CPU调度/clip_image001-1603973712207.png)

 

**答案：**

1. 先到先服务（FCFS）算法。
   β>α>0说明进程在队列中等待CPU和在运行时，优先级都在提高，都会比刚进入就绪队列的进程大，因此在队列中等待CPU的进程和运行的进程不会被刚进入的进程抢占；又因为β>α，运行的进程的优先级会始终大于在等待的进程的优先级，因此正在运行的进程不会被等待的进程抢占。

2. 后进先出（LIFO）算法。
   α<β<0说明进程在队列中等待CPU和在运行时，优先级都在降低，都会比刚进入就绪队列的进程小，因此在队列中等待CPU的进程和运行的进程会被刚进入的进程所抢占；又因为α<β，运行的进程的优先级会始终大于在等待的进程的优先级，因此正在运行的进程不会被等待的进程所抢占。