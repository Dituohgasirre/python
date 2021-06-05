<form class="form-content" action="/student/add" method="POST">
<div class="form-group">
  <input type="text" class="form-control" name="name" placeholder="学生姓名">
</div>

<div class="form-group">
<label class="radio-inline">
  <input type="radio" name="gender" value="1" checked> 男
</label>
<label class="radio-inline">
  <input type="radio" name="gender" value="0"> 女
</label>
</div>


<div class="form-group">
<input type="text" class="form-control" name="phone" placeholder="联系电话">
</div>

<div class="form-group">
<select name="sid" id="student-sid" class="form-control">
{sid_html}
</select>
</div>

<div class="form-group">
<select name="cid" id="student-cid" class="form-control">
  <option value="">所属班级</option>
</select>
</div>

<div class="form-group">
<textarea name="remark" class="form-control" rows="3" placeholder="备注"></textarea>
</div>

<button type="submit" class="btn btn-primary">添加</button>
</form>
