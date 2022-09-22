# SummerCamp2022_teamE

画像研夏合宿E班の開発用リポジトリです。 \
合宿なので、チーム開発に慣れてみるということで以下のような方針で簡単に進められたらと思います。 \
- 成果物のアップロード、進捗管理 ⇨ Github
- 最低限の開発環境の統一 ⇨ Docker 
- (Optional) Poetry

Dockerの使い方については以下が参考になりました。もし時間があれば見てみて下さい。
- [Docker日本語ドキュメント](https://docs.docker.jp/)
- 【図解】Dockerの全体像を理解する [[-前編-](https://qiita.com/etaroid/items/b1024c7d200a75b992fc)、[-中編-](https://qiita.com/etaroid/items/88ec3a0e2d80d7cdf87a)、[-後編-](https://qiita.com/etaroid/items/40106f13d47bfcbc2572)]


## Setup
ローカル環境にて、以下のスクリプトを実行して下さい。

### 1. リポジトリのクローン
```bash
git clone git@github.com:IkumaUchida/SummerCamp2022_teamE.git
cd SummerCamp2022_teamE
```
### 2. Docker image　の作成

```bash
make docker
```
このdocker imageの作成には通常5~10分かかります。コーヒーでも飲んで待っていて下さい。

### 3. Docker Containerの起動 & アタッチ
```bash
make docker-run
cd workspace/ #コンテナ内のターミナルで
```
これによりDockerコンテナ上で作業が可能となる。

 

## 開発規約
（規模的に不要ではありますが）合宿なので練習として，以下のルールにしたがって開発してみてください．

開発はissueベースで行います．
実装事項ができた際には，issueを立てる→issue IDでブランチを切る→実装後，githubへpushする→github上でdevelopブランチへのPull Requestを作成する．
機能追加は`feature/{タスク名}_{issueのID}`，修正は`fix/{タスク名}_{issueのID}`ブランチを切ってください．
例：
```
# issue IDが１のとき

# githubのリモートリポジトリと同期
$ git checkout master
$ git pull origin master

# ブランチ作成
$ git checkout -b feature/add_network_frame_#1

# 修正後，変更を追跡に追加しコミット
$ git add -A
$ git commit -m "add BaseVAE class"

# githubのリポジトリと動機
$ git push origin feature/add_network_frame_#1
```

コーディングルールはpysen準拠にします．
[pysen](https://github.com/pfnet/pysen)のチェックを通るようにしてからPull Requestを送るようにしてください．
```
# インストール
$ pip install "pysen[lint]"

# lintチェック
$ pysen run lint
$ pysen run format
```

pysen run lintとpysen run formatのフォーマットテストをクリアすると、以下のような出力が得られます。

`$ pysen run lint`

```bash
root@0600bb121552:/workspace# pysen run lint
Running commands concurrently...
... concurrent execution done
Running: black
Checking 0 files
Running: flake8
Checking 0 files
Running: isort
Checking 0 files

 ** execution summary **
isort .......... OK (0.14 sec)
black .......... OK (0.14 sec)
flake8 .......... OK (0.15 sec)
```


`$ pysen run format`

```bash
root@0600bb121552:/workspace# pysen run format
Running commands
Running: isort
Checking 0 files
Running: black
Checking 0 files

 ** execution summary **
isort .......... OK (0.14 sec)
black .......... OK (0.11 sec)
```

例えば、pysenでエラーが出ると以下のようなメッセージが出ます。

```bash
root@0600bb121552:/workspace# pysen run lint
... concurrent execution done
Running: black
Checking 1 files
--- /workspace/test_code.py     2022-09-19 16:14:10.482200 +0000
+++ /workspace/test_code.py     2022-09-22 07:17:44.042051 +0000
@@ -1 +1 @@
-print('Hi!')
+print("Hi!")
would reformat /workspace/test_code.py
Oh no! 💥 💔 💥
1 file would be reformatted.
Running: flake8
Checking 1 files
/workspace/test_code.py:1:13: W292 no newline at end of file
Running: isort
Checking 1 files

 ** execution summary **
isort .......... OK (1.74 sec)
black .......... Failed (1.73 sec)
flake8 .......... Failed (1.75 sec)

lint finished with error(s)
Errored:
 - black
 - flake8
 ```
