# SummerCamp2022_teamE

画像研夏合宿E班の開発用リポジトリです．
合宿なので、チーム開発に慣れてみるということで以下のような方針で簡単に進められたらと思います。
- 成果物のアップロード、進捗管理 ⇨ Github
- 最低限の開発環境の統一 ⇨ Docker 
- (Optional) Poetry

## Setup
準備中

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
