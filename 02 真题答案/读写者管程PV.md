# 读写者PV

想要写出读者优先的管程，先要理解读者优先的PV怎么写

首先读者优先的条件有

- 多个读者可以同时读（不需要互斥）
- 有读者等待时写者必须要等待（意味着必须要有一个int类型的数据来记录当前是否有读者等待，修改数据需要互斥修改，还要有一个互斥信号量）
- 有写者写时读者必须要等待（读者写者互斥）
- 写者之间也需要互斥（写者互斥）

明白了上述条件，我们可以初始定义这几个信号量

semaphore wm=1;  //读写者互斥

semaphore mutex=1;

int count=0;  //标记读者

那我们可以写出最初始的版本

```c
writer()
{
	while(1){
        P(wm);	//想要写
        writing...;
        V(wm);
    }
}
reader()
{
	while(1)
    {
   	 	P(mutex);	//读者之间的互斥
        count++;
        if(count==1)
            P(wm);	//已经有读者进来了，写者必须要等待
        V(mutex); 	
        reading...;
        P(mutex);
        count--;
        if(count==0)
            V(wm);	//当前退出的是最后一个读者，写者可以读了
        V(mutex);
    }
}
```

以上就是读者优先的PV版本，观察发现写者的逻辑很简单，那就是总是在尝试写，而读者的逻辑较复杂，因为必须要修改当前有多少个读者的记录，还要阻塞写者。

那么我们怎么把PV版本改成管程呢？首先还是要理解管程中的方法实质上就是PV中非临界区的代码的抽象，什么意思呢？假设我们已经完成了管程的编写，下面的代码就是我们想要借助管程而完成的效果

```c
writer()
{
    while(1)
    {
		start_write();//尝试写
        writing...;
        end_write();
    }
}
reader()
{
    while(1)
    {
        start_read();
        reading...;
        end_read();
    }
}
```

可以看到以上的代码相比较PV代码简洁了不少，原因就是管程通过各种各样的方法把非临界区的代码封装起来，对进程提供一个调用结果，大大提高了开发人员编写代码的效率。

那么重点来了，上面涉及到的四个函数，我们怎么才能把它写成管程的代码呢？

还是不要急，先让我们写出管程的框架吧

```c#
//假设管程中已经完成wait(),signal()方法的编写
monitor reader_writer{
	condition: wq,rq;//这里填上有多少种进程,本题中wq表示表示写进程，rq表示读进程
    //TODO:信号量的编写
    
    initialization_code()	//这里是信号量的初始代码
    {
        
    }
    void start_write(){
    	//TODO  
    }
    void end_write(){
		//TODO;
    }
    void start_read(){
        //TODO
    }
    void end_read(){
        //TODO
    }
}
```

好了，有了整体的框架，接下来我们先研究管程中有哪几个信号量吧

对读者来说：

- 需要标记当前有多少个读者——int rcount

对写者来说：

- 能不能写—— bool write_flag

有了以上两个信号量，我们先尝试着把写者的两个方法写了吧

```c
void start_write(){
    if(rcount>0||write_flag) //如果有读者，或者有其它写者
        wait(wq);	//阻塞该写者进程
    write_flag=true;	//可以写了，我先修改write_flag为true，提醒读者和其它写者现在轮到我了
}
void end_write(){
    write_flag=false;	//写完修改标记
    if(rq)signal(rq);	//读者优先，先叫醒管程中的读者
    else signal(wq);
}
```

好了，接下来我们可以编写读者的两个方法了

```c
void start_read(){
	if(write_flag)
        wait(rq);	//阻塞该读者进程
    rcount++;
    signal(rq);	//前面提到过读者进程可以同时读
}
void end_read(){
    rcount--;
    if(rcount==0)	//没有读者了，唤醒读者
        signal(wq);
}
```

接下来只剩最后一点工作了，那就是initialization_code()的编写

```c
void initialization_code()
{
    write_flag=false;
    rcount=0;
}
```

以上，我们就完成了读者优先管程代码的编写（完整版在最后）

现在我们来总结一下管程到底怎么写，在此之前，我们先回忆一下管程有什么特点吧

- 管程中任一时刻只有一个进程在执行，意味着管程中对自变量的修改不用加锁
- 管程通过wait和signal来阻塞和唤醒进程

把握住这两种特点，我们就有了对管程编写的思路了

1. 先分析题目中的互斥条件，主要是不同进程之间的互斥，相同进程之间的互持
2. 粗略的写出PV代码
3. **把非临界区封装成函数**
4. 编写管程中的信号量和初始化代码
5. 编写第3步函数的具体代码

许多读者不会写管程，实际上是少了2，3步的过程，直接编写管程过于困难。不过现在我们有了以上的例子，可以尝试着实现消费者管程，哲学家管程等经典问题的管程了。

---

完整版本，仅供参考

```c
//假设管程中已经完成wait(),signal()方法的编写
monitor reader_writer{
	condition: wq,rq;//这里填上有多少种进程,本题中wq表示表示写进程，rq表示读进程
    bool write_flag;
    int rcount;
    initialization_code()	//这里是信号量的初始代码
    {
        write_flag=false;
    	rcount=0;
    }
    void start_write(){
        if(rcount>0||write_flag) //如果有读者，或者有其它写者
            wait(wq);	//阻塞该写者进程
        write_flag=true;	//可以写了，我先修改write_flag为true，提醒读者和其它写者现在轮到我了
    }
    
    void end_write(){
        write_flag=false;	//写完修改标记
        if(rq)signal(rq);	//读者优先，先叫醒管程中的读者
        else signal(wq);
    }
    
    void start_read(){
	if(write_flag)
        wait(rq);	//阻塞该读者进程
    rcount++;
    signal(rq);	//前面提到过读者进程可以同时读
	}
    
    void end_read(){
        rcount--;
        if(rcount==0)	//没有读者了，唤醒读者
            signal(wq);
    }
}
```

