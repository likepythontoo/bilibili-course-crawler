# B站课程爬虫

这是一个用于爬取B站（哔哩哔哩）课程信息的Python程序。

## 功能特性

- ✅ 爬取课程详细信息（名称、发布者、价格、课时数、评分、章节数等）
- ✅ 支持多种课程类型（通识科普、IT互联网、生活兴趣等）
- ✅ 数据保存为JSON和CSV格式
- ✅ 错误处理和日志记录
- ✅ 请求头伪装和反爬虫策略
- ✅ 分页爬取支持

## 项目结构

```
bilibili-course-crawler/
├── README.md
├── requirements.txt
├── config.py          # 配置文件
├── crawler.py         # 主爬虫程序
├── data/             # 爬取数据存储目录
│   ├── courses.json
│   └── courses.csv
└── logs/             # 日志文件目录
```

## 安装与使用

### 1. 克隆仓库
```bash
git clone https://github.com/likepythontoo/bilibili-course-crawler.git
cd bilibili-course-crawler
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置参数
编辑 `config.py` 文件，设置要爬取的课程类型和其他参数。

### 4. 运行爬虫
```bash
python crawler.py
```

## 爬取信息字段

每条课程记录包含以下字段：
- `course_id` - 课程ID
- `course_name` - 课程名称
- `course_type` - 课程类型
- `publisher` - 发布者/讲师
- `price` - 价格
- `duration` - 课时数
- `rating` - 评分
- `rating_count` - 评分人数
- `chapter_count` - 章节数
- `description` - 课程描述
- `url` - 课程链接
- `update_time` - 更新时间

## 注意事项

⚠️ 本项目仅供学习和研究使用，请遵守B站的服务条款和robots.txt。
⚠️ 爬虫会设置合理的请求延迟，避免对服务器造成压力。
⚠️ 请勿用于商业用途。

## 依赖库

- requests - HTTP请求库
- beautifulsoup4 - HTML解析库
- pandas - 数据处理库
- python-dotenv - 环境变量管理

## 许可证

MIT License

## 作者

likepythontoo