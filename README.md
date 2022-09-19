# SummerCamp2022_teamE

画像研夏合宿E班の開発用リポジトリです。 \
合宿なので、チーム開発に慣れてみるということで以下のような方針で簡単に進められたらと思います。 \
- 成果物のアップロード、進捗管理 ⇨ Github
- 最低限の開発環境の統一 ⇨ Docker 
- (Optional) Poetry

Dockerの使い方については以下が参考になりました。もし時間があれば見てみて下さい。
- 

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
- *補足*
使用している環境によっては、`make docker`でエラーが発生しimageが作成出来ない場合があります。 
その場合は、環境に合わせて[`Dockerfile`](https://github.com/IkumaUchida/SummerCamp2022_teamE/blob/main/Dockerfile)を書き換えて下さい。　\
`cuda:11.3.0`や`ubuntu20.04`や`cu113`の数字の部分です。

例 : OSがUbunts20.04でcudaのバージョンが11.3.０の場合

```dockerfile
FROM  nvidia/cuda:11.3.0-cudnn8-devel-ubuntu20.04　＃＃１行目

~~~

# For pytorch
RUN pip3 install torch==1.10.1+cu113 torchvision==0.11.2+cu113 torchaudio==0.10.1+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html #40行目

```

### . Docker Containerの起動 & アタッチ
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
