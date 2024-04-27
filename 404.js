// 显示弹窗
window.onload = function() {
    var modal = document.createElement('div');
    modal.classList.add('modal');
    modal.innerHTML = '<p>似乎出现了一些不可控问题导致您进入了这个错误界面,不过没关系,您即将在 7秒 之后回到『硫酸铝的个人网站』主界面!<br>如果您反复遇见这个界面,那么请联系 Al2(SO4)3-硫酸铝 提交问题,我们十分感谢您的支持与反馈!</p>';
    document.body.appendChild(modal);
    modal.style.display = 'block';
    setTimeout(function() {
      modal.style.display = 'none';
    }, 7000); // 7秒后自动隐藏
  };
// 使用 setTimeout 函数在页面加载后经过 7 秒自动跳转到指定页面
setTimeout(function() {
      window.location.href = 'https://al2so43.github.io/website'; // 替换为您要跳转的页面地址
  }, 7000); // 7秒后跳转