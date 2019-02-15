<?php
//用类模拟node节点
class node {
    private $value = -1;
    private $next = null;
    public function __construct($v,$next)
    {
        $this->value = $v;
        $this->next = $next;
    }
    public function __set($name,$value)
    {
        $this->$name = $value;
    }
    public function __get($name) 
    {
        return $this->$name;
    }
}

class Eliminate 
{
    private $maxNum;
    private $nowNum; 
    private $times;
    private $maxAge;
    //表头
    private $head = null;

    public function __construct($params)
    {
        $this->maxNum = $params[1];
        $this->nowNum = $params[2];
        $this->times = $params[3];
        $this->maxAge = $params[4];
        //初始化链表
        $this->initList();
    }

    private function initList()
    {
        $preNode = null;
        for ($i = $this->nowNum - 1;$i >= 0; $i--) {
            $preNode = new node(mt_rand(0,10),$preNode);
        }
        $this->head = $preNode;
        echo "init list data:\n";
        $this->printNode();
    }


    protected function del($node)
    {
        unset($node);
    }

    public function run()
    {
        $i = $this->times;
        while ($i-- > 0) {
            $this->does();
            sleep(1);
        }
    }

    private function printNode()
    {
        $temp = $this->head;
        while ($temp != null) {
            echo $temp->value." ";
            $temp = $temp->next;
        }
        echo "list now  num : $this->nowNum \n";
    }

    private function does()
    {
        //先把所有的age给加1,flag标识是否删除了节点
        $flag = 0;
        $temp = $this->head;
        $preNode = null;
        while ($temp != null) {
            $value = ++$temp->value;
            //判断每个age是否超过阈值,flag标识是否删除过
            if ($value > 10 && $flag == 0) {
                if ($preNode) {
                    $preNode->next = $temp->next;
                } else {
                    $this->head = $temp->next;
                }
                echo "超过阈值，删除节点\t";
                $flag = 1;
                $this->nowNum--;
            }
            $preNode = $temp;
            $temp = $temp->next;
        }

        //如果没有删除过节点 则删除第一个节点
        if ($flag == 0 && $this->nowNum >= $this->maxNum) {
            $this->nowNum--;
            $this->head = $this->head->next;
            echo "删除第一个节点\t";
        }

        //要插入的位置
        $position = rand(1,$this->nowNum);
        //插入节点
        $temp = $this->head;
        $i = 0;
        echo "插入节点随机位置：".$position."\t\n";
        $preNode = null;
        while ($temp != null) {
            if ($i == $position - 1) {
                if ($i == 0) {
                    //表头
                    $this->head = new node(0,$this->head);
                } else {
                    $preNode->next = new node(0,$preNode->next);
                }
                $this->nowNum++;
            }
            $i++;
            $preNode = $temp;
            $temp = $temp->next;
        }
        $this->printNode();
    }
}


function main($argc, $argv) {
    $argv[1] = isset($argv[1]) ? $argv[1] : 10;
    $argv[2] = isset($argv[2]) ? $argv[2] : 5;
    $argv[3] = isset($argv[3]) ? $argv[3] : 200;
    $argv[4] = isset($argv[4]) ? $argv[4] : 10;
    $elim = new Eliminate($argv);
    $elim->run();
}

//第一个参数 链表最大长度;第二个参数 链表初始长度;第三个参数 多少秒;第四个参数 淘汰的最大age (所有参数均有默认值)
main($argc, $argv);
