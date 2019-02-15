<?php
class Path
{
    private $arr = [
        'A'=>['value'=>'A','child_list'=>['B','C','D']],
        'B'=>['value'=>'B','child_list'=>['E','F','G']],
        'C'=>['value'=>'C','child_list'=>[]],
        'D'=>['value'=>'D','child_list'=>['H','I','J']],
        'E'=>['value'=>'E','child_list'=>[]],
        'F'=>['value'=>'F','child_list'=>['K','L','N']],
        'G'=>['value'=>'G','child_list'=>[]],
        'H'=>['value'=>'H','child_list'=>['O','P','Q']],
        'I'=>['value'=>'I','child_list'=>[]],
        'J'=>['value'=>'J','child_list'=>[]],
        'K'=>['value'=>'K','child_list'=>[]],
        'L'=>['value'=>'L','child_list'=>[]],
        'N'=>['value'=>'N','child_list'=>['R','S','T']],
        'O'=>['value'=>'O','child_list'=>[]],
        'P'=>['value'=>'P','child_list'=>[]],
        'Q'=>['value'=>'Q','child_list'=>[]],
        'R'=>['value'=>'R','child_list'=>[]],
        'S'=>['value'=>'S','child_list'=>[]],
        'T'=>['value'=>'T','child_list'=>[]],
    ];

    private function findRoot($key,$root = [])
    {
        foreach ($this->arr as $k => $v) {
            if (in_array($key,$v['child_list'])) {
                $root[] = $k;
                return $this->findRoot($k,$root);
            }
        }
        return $root;
    }

    public function run($argc, $argv)
    {
        $rootNode1 = $this->findRoot($argv[1]);
        $rootNode2 = $this->findRoot($argv[2]);
        if (!$rootNode1) {
            $rootNode1[] = $argv[1];
        } else {
            $printNode1[] = $argv[1]; 
        }
        if (!$rootNode2) {
            $rootNode2[] = $argv[2];
        } else {
            $printNode2[] = $argv[2];
        }
        foreach ($rootNode1 as $k => $v) {
            $printNode1[] = $v;
            if (in_array($v, $rootNode2)) {
                foreach ($rootNode2 as $k1 => $v1) {
                    if ($v1 == $v) {
                        break;
                    } else {
                        $printNode2[] = $v1;
                    }
                }
                if ($printNode2) {
                    $printNode2 = array_reverse($printNode2);
                }
                break;
            }
        }
        echo implode('->',$printNode1);
        echo '->';
        echo implode('->',$printNode2);
        echo "\n";
    }
}

$path = new Path();
//参数验证省略,假设合法
$path->run($argc, $argv);
