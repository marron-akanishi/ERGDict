# エロゲタイトル変換辞書  
Google日本語入力でエロゲのタイトルを変換出来るようにする辞書。  
1995年以降の非抜きゲーのみを対象としています。 
コメントとしてブランド名を入れてあります。 
## 使用方法
Google日本語入力の辞書ツールから管理→新規辞書にインポートを選択して、ファイルで辞書テキストファイルを選択する。  
辞書名を適当につけてからそのままインポートをクリックする。  
自動出力なのでエラーが発生して、インポート件数が辞書ファイルより少なくなるが問題はないと思われる。  
更新時は作成した辞書を選択して、管理→選択した辞書にインポートを選択、ファイルを指定すれば追加されていく。
## 変換に必要なもの

- Python3
- Beautiful Soup4(HTMLの切り出しに使用)
- jaconv(カタカナ→ひらがな変換に使用)

## リスト作成方法  
[SQL実行フォーム -エロゲーマーのためのSQL-](https://goo.gl/WBuoeB)で以下のSQL文を実行  
```SQL  
SELECT g.furigana,g.gamename,b.brandname
FROM gamelist g
INNER JOIN brandlist b
ON b.id = g.brandname
WHERE sellday >= '1995-01-01'
AND sellday <> '2030-01-01'
AND okazu = 'f'
ORDER BY furigana
```  
出力結果のHTMLを保存し、source.htmlにコピーした後にmake_title.pyを実行する。  
すると辞書がergtitle.txtとして出力される。  
## 出力形式  
Google日本語入力で辞書としてインポート出来る形式  
読み[tab]タイトル[tab]固有名詞という感じで一行ずつ並んで出力される。  
### メモ
_brandはブランド一覧出力用  
```SQL  
SELECT brandfurigana,brandname
FROM brandlist
WHERE kind = "CORPORATION"
AND lost = "FALSE"
ORDER BY brandfurigana
```