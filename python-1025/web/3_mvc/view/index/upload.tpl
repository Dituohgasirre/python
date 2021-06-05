<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>上传文件演示</title>
    <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
    <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
  </head>
  <body>
    <div class="container" id="body">

<form action="/index/upload" method="post" enctype="multipart/form-data">
<!-- <form action="/index/upload" method="post"> -->
  <div class="form-group">
    <label for="exampleInputEmail1">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Email" name="email" value="iprintf@qq.com">
  </div>
  <div class="form-group">
    <label for="exampleInputPassword1">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password" name="pass" value="123">
  </div>
  <div class="form-group">
    <label for="exampleInputFile">File input</label>
    <input type="file" id="exampleInputFile" name="upfile">
    <p class="help-block">Example block-level help text here.</p>
  </div>
  <div class="checkbox">
    <label class="checkbox-inline">
      <input type="checkbox" name="check" value="1" checked> Check 1
    </label>
    <label class="checkbox-inline">
      <input type="checkbox" name="check" value="2" checked> Check 2
    </label>
    <label class="checkbox-inline">
      <input type="checkbox" name="check" value="3" checked> Check 3
    </label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>

    </div>
    <!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
    <script src="https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
  </body>
</html>
