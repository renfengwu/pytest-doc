# pytest 快速上手示例

一个最小化的 pytest 演示项目，包含一个简单的计算器模块和对应的测试用例。

## 目录结构

```
pytest_doc/
├── src/
│   └── calculator.py        # 被测代码：加减乘除 + 判断偶数
├── tests/
│   └── test_calculator.py   # 测试用例：断言 / 异常 / 参数化 / fixture
├── pytest.ini               # pytest 配置
├── pyproject.toml           # ruff（lint + format）配置
├── requirements.txt         # 依赖
└── README.md
```

## 环境准备

```bash
# 1. （可选）创建并激活虚拟环境
python -m venv venv
# Windows PowerShell:
venv\Scripts\Activate.ps1
# Linux / macOS:
source venv/bin/activate

# 2. 安装依赖
pip install -r requirements.txt
```

## 开发人员如何运行 pytest

在项目根目录 `pytest_doc/` 下执行：

| 目的 | 命令 |
| --- | --- |
| 运行全部测试 | `pytest` 或 `python -m pytest` |
| 详细输出（显示每个用例） | `pytest -v` |
| 只运行某个文件 | `pytest tests/test_calculator.py` |
| 只运行某个用例 | `pytest tests/test_calculator.py::test_add` |
| 按名称关键字筛选 | `pytest -k "divide"` |
| 遇到第一个失败就停止 | `pytest -x` |
| 显示 print 输出 | `pytest -s` |
| 查看测试结果摘要 | `pytest -ra` |
| 生成覆盖率报告（需 pytest-cov） | `pytest --cov=src` |

> 推荐使用 `python -m pytest`，它会把当前目录加入 `sys.path`，避免导入路径问题。

## 预期结果

```
============================= test session starts =============================
collected 11 items

tests/test_calculator.py::test_add PASSED                                [  9%]
...
============================= 11 passed in 0.08s ==============================
```

## 代码检查（ruff：lint + 格式化）

[ruff](https://docs.astral.sh/ruff/) 是一个用 Rust 写的高性能工具，**一个工具同时替代 flake8（lint）+ isort（导入排序）+ black（格式化）**。配置写在 `pyproject.toml` 里。

在项目根目录 `pytest_doc/` 下执行：

| 目的 | 命令 |
| --- | --- |
| 检查代码问题（lint） | `ruff check .` |
| 自动修复可修复的问题 | `ruff check --fix .` |
| 检查格式（不修改文件） | `ruff format --check .` |
| 自动格式化代码 | `ruff format .` |

> 推荐流程：先 `ruff check --fix .` 修 lint，再 `ruff format .` 统一格式，最后 `pytest` 跑测试。
> 启用的规则集：`E/W`(PEP8) `F`(pyflakes) `I`(isort) `B`(bugbear) `UP`(pyupgrade)。

### 一键质量检查

```bash
ruff check . && ruff format --check . && pytest
```

CI 流水线里通常就是这一行：任意一步失败则整体失败。

## 示例中演示的 pytest 核心知识点

1. **基本断言**：直接用 Python 的 `assert`，pytest 会自动给出详细的失败信息。
2. **异常断言**：`with pytest.raises(ValueError, match="..."):` 校验函数是否按预期抛异常。
3. **参数化** `@pytest.mark.parametrize`：一份测试逻辑跑多组输入/输出数据。
4. **fixture** `@pytest.fixture`：为测试提供可复用的前置数据或资源。
