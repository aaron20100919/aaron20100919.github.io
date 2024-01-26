<?php
// 请将路径调整为存储图像的实际文件夹
$imageDirectory = 'pic';

// 获取图像文件列表
$imageFiles = glob($imageDirectory . '/*.jpg');

// 生成一个随机索引
$randomIndex = mt_rand(0, count($imageFiles) - 1);

// 获取随机图像文件名
$randomImageFileName = basename($imageFiles[$randomIndex]);

// 构建图像文件的完整路径
$imagePath = $imageDirectory . '/' . $randomImageFileName;

// 设置响应头，指示返回的是图像
header('Content-Type: image/jpeg');

// 发送图像文件
readfile($imagePath);
?>
