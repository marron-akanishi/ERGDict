# エロゲタイトル変換辞書  
Google日本語入力でエロゲのタイトルを変換出来るようにする辞書。  
1995年以降の非抜きゲーのみを対象としています。  
## 変換に必要なもの

- Python3
- Beautiful Soup4(HTMLの切り出しに使用)
- jaconv(カタカナ→ひらがな変換に使用)
## リスト作成方法  
[SQL実行フォーム -エロゲーマーのためのSQL-](https://goo.gl/WBuoeB)で以下のSQL文を実行  
```SQL  
SELECT furigana,gamename 
FROM gamelist  
WHERE sellday >= '1995-01-01'  
AND sellday <> '2030-01-01'  
AND okazu = 'f'  
ORDER BY furigana  
```  
出力結果のHTMLを保存し、source.htmlにコピーした後にmake.pyを実行する。  
すると辞書がergtitle.txtとして出力される。  
## 出力形式  
Google日本語入力で辞書としてインポート出来る形式  
読み[tab]タイトル[tab]固有名詞という感じで一行ずつ並んで出力される。  