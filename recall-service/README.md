# Recall Service for Concrec

## 运行环境配置
- 安装Docker，并运行 `docker run --name recall-redis -d -p 6379:6379 redis`
- 首先请保证系统装有python3以及virtualenv
- 在项目目录下初始化虚拟环境: `virtualenv venv --python=python3`
- 加载虚拟环境`source venv/bin/activate`
- `pip install -r requirements.txt`

## Run
- `source venv/bin/activate`
- `./start.sh`

## API
- `GET` `/?user_id=<uid>`
  - Get recall for a user
  - Returns list of anime ids


- `GET` `/sim?anime_id=<aid>`
  - Get similar items for an anime
  - Returns list of anime ids
