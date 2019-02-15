<?php
function getAllfile($folder) {
    $arrFile = [];
    $handle = opendir($folder);
    while (($file = readdir($handle)) !== false) {
        if ($file == '.' || $file == '..') {
            continue;  
        }
        if (is_file($folder."/".$file)) {
            $file = $folder."/".$file; 
            $arrFile[] = $file;
        } elseif (is_dir($folder."/".$file)) {
            $file = $folder."/".$file; 
            $arrFile[$file] = getAllfile($file);
        }
    }
    closedir($handle);
    return $arrFile;

}
$a = getAllfile("/home/vagrant/c");
var_dump($a);
