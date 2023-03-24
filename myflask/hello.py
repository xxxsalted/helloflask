import os
import flask
from forms import LoginForm

app = flask.Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


@app.context_processor
def pre_data():
    name = 'Edison'
    articles = [
        {'title': 'Linux Bash Shell 中变量的 5 个易错点',
         'link': 'https://mp.weixin.qq.com/s?__biz=MzkzNzI1MzE2Mw==&mid=2247485191&idx=1&sn=66d5df64237702f739653fc96214e9f6&chksm=c2930743f5e48e55c453c1eaab411032564d74aec92c9540ad0e42ca4040d9a3bc164a6a5255&token=594580428&lang=zh_CN#rd'},
        {'title': '为什么文件删除了但磁盘空间没有释放？',
         'link': 'https://mp.weixin.qq.com/s?__biz=MzkzNzI1MzE2Mw==&mid=2247485173&idx=1&sn=1fd1eb7ce263fffe02a0cbe137dc20f6&chksm=c29306b1f5e48fa75cef000fdd44839a68896fb4921a711a4ad0aa8369cb5192e933638f7d9a&token=594580428&lang=zh_CN#rd'},
        {'title': '分享几个常用的运维 shell 脚本',
         'link': 'https://mp.weixin.qq.com/s?__biz=MzkzNzI1MzE2Mw==&mid=2247485124&idx=1&sn=fcdb9ce473aae67ed7c759839018395c&chksm=c2930680f5e48f96ebcf98f11540af4b261fee30dccaf9f6ccf632d447bd393cd6b7bb1aa2fa&token=594580428&lang=zh_CN#rd'},
        {'title': '干货！超实用的 Linux 初始化脚本',
         'link': 'https://mp.weixin.qq.com/s?__biz=MzkzNzI1MzE2Mw==&mid=2247485124&idx=1&sn=fcdb9ce473aae67ed7c759839018395c&chksm=c2930680f5e48f96ebcf98f11540af4b261fee30dccaf9f6ccf632d447bd393cd6b7bb1aa2fa&token=594580428&lang=zh_CN#rd'},
        {'title': '跟女朋友介绍十个常用的 Python 内置函数，她夸了我一整天',
         'link': 'https://mp.weixin.qq.com/s?__biz=MzkzNzI1MzE2Mw==&mid=2247485052&idx=1&sn=6a3d7198aa107cd6c8b14b23660172b7&chksm=c2930638f5e48f2e792b1586f67563a76f57870f72aa8e639625dd748b660100a6175ee5d991&token=594580428&lang=zh_CN#rd'},
        {'title': '99%运维人员都忽略的服务器安全问题',
         'link': 'https://mp.weixin.qq.com/s?__biz=MzkzNzI1MzE2Mw==&mid=2247484981&idx=1&sn=4f61787682d0b4924f7920d5e68d9bdb&chksm=c2930671f5e48f678d0e76bbb0b51252c266b3165695dc82d0d7852c61500a96eb3fc6909a37&token=594580428&lang=zh_CN#rd'},
        {'title': 'Python 网络编程',
         'link': 'https://mp.weixin.qq.com/s?__biz=MzkzNzI1MzE2Mw==&mid=2247484949&idx=1&sn=311cb4d57ccd8fc9396b0b53d64cd8bf&chksm=c2930651f5e48f4785129241943d0938431d9792d3ab6d566c67b4b1a80953e7c43cf3fef446&token=594580428&lang=zh_CN#rd'},
        {'title': 'Python爬虫实战(5) | 爬取知网文献信息',
         'link': 'https://mp.weixin.qq.com/s?__biz=MzkzNzI1MzE2Mw==&mid=2247484778&idx=1&sn=c349d35c88ceffd7ef6505d2165dcbfc&chksm=c293052ef5e48c38ad95e81ea6b8627909d361ce1e39675fa777677b049fb6a85b4feca34b2a&token=594580428&lang=zh_CN#rd'},
        {'title': 'Python爬虫实战(4) | 爬取历年中国电影票房排行榜',
         'link': 'https://mp.weixin.qq.com/s?__biz=MzkzNzI1MzE2Mw==&mid=2247484700&idx=1&sn=fc3da783f37ea6f353cbe512039791c0&chksm=c2930558f5e48c4e3a408d5fb9d447893ac46bf1851d8877dee3fa55a23ba3b52f510454ddb8&token=594580428&lang=zh_CN#rd'},
        {'title': '2023开工大吉',
         'link': 'https://mp.weixin.qq.com/s?__biz=MzkzNzI1MzE2Mw==&mid=2247484783&idx=1&sn=b8f3d8fd46b14a789cc6960c0bb8e95b&chksm=c293052bf5e48c3d81e8210070525d15ea4af8026b6ca14349c00f1c797453a24dacb6928b01&token=594580428&lang=zh_CN#rd'},
    ]

    return dict(name=name, articles=articles)


@app.before_request
def get_name():
    flask.g.name = flask.request.args.get('name')


@app.template_filter()
def heart(str):
    return str + flask.Markup(' &hearts;')


@app.route('/')
@app.route('/index')
def index():
    title = 'Home'
    form = LoginForm()
    return flask.render_template('index.html', title=title, form=form)


@app.route('/watchlist')
def watchlist():
    title = 'Watclhlist'
    return flask.render_template('watchlist.html', title=title)


@app.route('/flash')
def flash_msg():
    flask.flash("I am Flash!")
    return flask.redirect(flask.url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('/errors/404.html'), 404

