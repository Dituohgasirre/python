<form class="form-content" action="/student/modify" method="POST">
<div class="form-group">
  <input type="text" class="form-control" name="name" placeholder="学生姓名" value="{name}">
</div>

<div class="form-group">
<label class="radio-inline">
  <input type="radio" name="gender" value="1" {gender1}> 男
</label>
<label class="radio-inline">
  <input type="radio" name="gender" value="0" {gender0}> 女
</label>
</div>


<div class="form-group">
<input type="text" class="form-control" name="phone" value="{phone}" placeholder="联系电话">
</div>

<div class="form-group">
<select name="sid" id="student-sid" class="form-control">
{sid_html}
</select>
</div>

<div class="form-group">
<select name="cid" id="student-cid" class="form-control">
{cid_html}
</select>
</div>

<div class="form-group">
<textarea name="remark" class="form-control" rows="3" placeholder="备注">{remark}</textarea>
</div>

<input type="hidden" name="id" value="{id}">

<button type="submit" class="btn btn-primary">更新</button> &emsp; &emsp;
<button type="button" class="btn btn-primary" onclick="history.go(-1)">返回</button>
</form>
