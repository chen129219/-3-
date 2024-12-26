此代码通过随机生成100至255之间的素数，计算原根，并进行相应的计算，word文档中记录的是随机选择十次素数计算的过程结果。

下面是关于代码的简要说明：

生成素数列表：
generate_primes(start, end) 函数用于生成指定范围内的素数。
通过检查一个数是否有因子来判断其是否为素数。


检查原根：
is_primitive_root(g, p) 函数用于确定某个数 g 是否为模 p 的原根。
它通过计算某个数 g 的所有幂次模 p 的不同余数来进行验证，这个集合如果与小于 p 的互素数集合相同，则 g 是原根。

gcd(a, b) 函数用于计算两个数的最大公约数

Diffie-Hellman 主程序：
首先程序生成一个素数列表 primes 并从中随机选择一个素数 p。
然后尝试找到一个 p 的原根 g。
成员 A 和 B 分别选取他们的私钥 a 和 b。
计算各自的公钥 A_pub 以及 B_pub。
A 计算共享密钥 S_A 和 B 计算共享密钥 S_B。
最后，若两个参与方计算出的共享密钥一致，表明密钥交换成功。

下面为实验结果：

随机生成的素数为167时，原根为5时计算结果为
![image](https://github.com/user-attachments/assets/2e9f4f37-4a57-44ea-a92f-d60af32f56e7)

 
随机生成的素数为241时，原根为7时计算结果为
![image](https://github.com/user-attachments/assets/4a762392-761b-4a57-99ee-8b4c17a69584)

 
随机生成的素数为227时，原根为2时计算结果为
![image](https://github.com/user-attachments/assets/2de560a8-6493-4b22-9fd0-757133718062)

 
随机生成的素数为157时，原根为5时计算结果为
![image](https://github.com/user-attachments/assets/858b50de-23f1-47bc-a94a-7d02d696ae17)

 
随机生成的素数为131时，原根为2时计算结果为
![image](https://github.com/user-attachments/assets/d8d93189-1345-4b2a-b4c3-7073061ddc8c)

 
随机生成的素数为127时，原根为3时计算结果为
![image](https://github.com/user-attachments/assets/277bc855-b200-4e4d-86f0-641ec23047d3)

 
随机生成的素数为197时，原根为2时计算结果为
![image](https://github.com/user-attachments/assets/15e8c623-0708-472a-8534-d3adb63b5fbf)

 
随机生成的素数为137时，原根为3时计算结果为
![image](https://github.com/user-attachments/assets/ff3d2d8d-9c48-40d3-90c2-dade60d57c93)

 
随机生成的素数为107时，原根为2时计算结果为
 ![image](https://github.com/user-attachments/assets/0891bb29-e632-4cc4-8cd2-cfbaff72f393)
