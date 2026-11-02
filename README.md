# AI Agent积分活动留存设计工作流
从TeleAgent设计测试题沉淀，目标是将积分活动迁移到不同Agent产品。

## 使用
将 ai-agent-design-workflow 目录作为skill加载，提供真实产品截图、能力证据和业务目标。填写 fixtures 风格的适配参数。执行 `python3 -m unittest discover -s tests -v`。

## 当前验证范围
TeleAgent、Open Design、AutoClaw三份规则配置和领取状态模拟；Open Design本地界面原型。没有真实发奖接口、后台接入或线上留存数据。规则模拟通过不等于通用性已充分证明。

## 发布范围
仅工作流、合成配置、测试和自建原型适合本仓库。不包含用户邮件、原提交PDF、第三方IP素材、真实账号和密钥。无默认开源许可证，公开发布前由仓库所有者选择。

## 验证命令
`python3 -m unittest discover -s tests -v`

`node tests/test_prototype.cjs`

回归命令可本地运行；ci/validate-workflow.yml.example 是待仓库所有者启用的Actions模板，当前OAuth缺少workflow权限，未启用远端CI。网页可手动打开 prototype/index.html，五个状态页通过顶部导航切换；次日解锁是测试控制，不是正式用户功能。

## 待完成
Figma测试目标：https://www.figma.com/design/lUdYWTs5kc0yoQhepzKYYn/skill测试?node-id=0-1 。目前连接受阻，尚未生成节点。视觉与浏览器真实点击未验收，线上效果未验证。
