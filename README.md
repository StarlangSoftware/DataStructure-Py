# DataStructure

For Developers
============
You can also see [Java](https://github.com/olcaytaner/DataStructure), [C++](https://github.com/olcaytaner/DataStructure-CPP), or [C#](https://github.com/olcaytaner/DataStructure-CS) repository.

## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called DataStructure will be created. Or you can use below link for exploring the code:

	git clone https://github.com/olcaytaner/DataStructure-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `DataStructure-PY` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 


## Compile

**From IDE**

After being done with the downloading and Maven indexing, select **Build Project** option from **Build** menu. After compilation process, user can run DataStructure.

Detailed Description
============
+ [CounterHashMap](#counterhashmap)
+ [LRUCache](#lrucache)

## CounterHashMap

CounterHashMap bir veri tipinin kaç kere geçtiğini hafızada tutmak için kullanılmaktadır.

Bir CounterHashMap yaratmak için

	a = CounterHashMap()

Hafızaya veri eklemek için

	put(self, key: object)

Örneğin,

	a.put("ali");

Bu aşamanın ardından "ali" nin sayacı 1 olur.

Hafızaya o veriyi birden fazla kez eklemek için

	putNTimes(self, key: object, N: int)

Örneğin,

	a.putNTimes("veli", 5)

Bu aşamanın ardından "ali"'nin sayacı 5 olur.

Hafızada o verinin kaç kere geçtiğini bulmak için

	count(self, key: object) -> int

Örneğin, "veli" nin kaç kere geçtiğini bulmak için

	kacKere = a.count("veli")

Bu aşamanın ardından kacKere değişkeninin değeri 5 olur.

Hafızada hangi verinin en çok geçtiğini bulmak için

	max(self) -> object

Örneğin,

	kelime = a.max()

Bu aşamanın ardından kelime "veli" olur.

## LRUCache

LRUCache veri cachelemek için kullanılan bir veri yapısıdır. LRUCache en yakın zamanda 
kullanılan verileri öncelikli olarak hafızada tutar. Bir LRUCache yaratmak için

	LRUCache(self, cacheSize: int)

kullanılır. cacheSize burada cachelenecek verinin büyüklüğünün limitini göstermektedir.

Cache'e bir veri eklemek için

	add(self, key: object, data: object)

kullanılır. data burada eklenecek veriyi, key anahtar göstergeyi göstermektedir.

Cache'de bir veri var mı diye kontrol etmek için

	contains(self, key: object) -> bool

kullanılır.

Cache'deki veriyi anahtarına göre getirmek için

	get(self, key: object) -> object

kullanılır.

