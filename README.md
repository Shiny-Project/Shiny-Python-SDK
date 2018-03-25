# Shiny Python SDK

## 安装
`pip install Shiny_SDK`


## 初始化

```Python
import Shiny

shiny  = Shiny.Shiny(API_KEY, API_SECRET_KEY, API_HOST = 'https://shiny.kotori.moe')
```

请注意，API_HOST有默认值，如果需要手工指定，最后不要带斜杠。

## 方法

### `shiny.add(spider_name, level, data, hash=None)`

向Shiny提交一个新的事件

参数说明：

| 参数名 | 参数类型 | 参数说明 |
| ------|-------|-----------|
| spider_name| string | spider标识符|
| level | int | 事件等级（1~5）|
| data | dict  | 事件内容 包括 title、link、cover、content|
| hash | string | 事件 Hash (可选，不指定会自动生成) |


如果失败会抛出一个`ShinyError`，请注意捕获。

### `shiny.add_many(events)`

批量添加事件

参数说明：

| 参数名 | 参数类型 | 参数说明 |
| ------|-------|-----------|
| events | list | 事件们  |

`events`参数应是`event`的列表，请参照`shiny.add()`的小节。

### `shiny.recent()`

查询最新事件，返回一个`list`。

### `shiny.get_jobs()`

获得任务列表。