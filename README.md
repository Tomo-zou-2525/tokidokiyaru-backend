# tokidokiyaru-backend

# ローカル開発環境

## 概要
[VSCode Remote Container](https://code.visualstudio.com/docs/remote/containers)を利用している。

- コンテナ内で開発できるためローカルのプロセスやネームスペースから切り離した環境で開発が可能
- またローカル環境はVSCodeとDockerが入っていればそれ以外のもののインストールは不要
- リンター、フォーマッター、VSCodeの拡張機能の設定がgitで管理されるため共有が可能
- 等々

## 必要なもの
- [Docker Descktop](https://www.docker.com/products/docker-desktop/)
- [VSCode](https://azure.microsoft.com/ja-jp/products/visual-studio-code)

## ローカル環境構築手順
- Docker Descktopを起動する
- VSCodeのDev Containers(`ms-vscode-remote.remote-containers` )拡張機能をインストールする
- `⌘ + shift + p` で `Dev Containers: Open Folder in Container...` を選択、カレントディレクトリでDev Containersを立ち上げる
