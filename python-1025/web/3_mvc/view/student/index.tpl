<ol class="breadcrumb">
  <li><a href="#">学校管理平台</a></li>
  <li><a href="#">学生管理</a></li>
</ol>

<div class="row search-row">
  <div class="col-lg-6 col-lg-offset-3">
    <div class="input-group">
      <input class="form-control" id="search" type="text" placeholder="请输入查询关键词..." value="{search}">
      <span class="input-group-btn"><button class="btn btn-primary btn-search"><span class="glyphicon glyphicon-search"></span></button></span>
    </div>
  </div>
</div>

<div class="row op-row">
  <div class="col-lg-10">
    <button class="btn btn-primary btn-add-student">添加学生</button>
  </div>
  <div class="col-lg-2 text-right">
    <!-- Single button -->
    <div class="btn-group">
      <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
        批量操作 <span class="caret"></span>
      </button>
      <ul class="dropdown-menu">
        <li><a href="#">删除</a></li>
        <li role="separator" class="divider"></li>
        <li><a href="#">锁定</a></li>
      </ul>
    </div>
  </div>
</div>

<div class="table-responsive text-center">
  <table class="table table-striped table-bordered">
    <thread>
    <tr>
      <th><input type="checkbox"></th>
      <th>学号</th>
      <th>姓名</th>
      <th>班级</th>
      <th>学校</th>
      <th>操作</th>
    </tr>
    </thread>
    <tbody>
      {student_list}
    </tbody>
  </table>
  {page_html}
</div>

