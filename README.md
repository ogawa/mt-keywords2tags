# mt-keywords2tags

エントリーのキーワードをMT 3.3以降のタグにコンバートするCGIスクリプト。

## 更新履歴

 * 0.01 (2006.06.05):
   * 作成。

## 概要

Tags Plugin, Tagwire Plugin, Tags.Appなどのプラグインは、Movable Typeのエントリーのキーワード欄をタグ入力欄として使用していましたが、このキーワードをMovable Type 3.3以降のタグにコンバートするための簡単なCGIスクリプトです。

## 使い方

使用に先立って転送元のDBのバックアップを取っておいてください。

mt-keywords2tags.cgiをmt.cgiなどと同じディレクトリにコピーし、実行パーミッションを設定します。

Webブラウザを使ってmt-keywords2tags.cgiにアクセスすると変換処理が始まります。「Successfully added tags.」と表示されたら完了です。

    mt-keywords2tags
    
    1: About
    4: Housing, Moving
    12: Research, Trip, Hokkaido
    23: Research, Trip, Paris
    ...
    
    Successfully added tags.

mt.cgiにアクセスして各エントリーにタグ情報が追加されているかどうか確認しましょう。あとは再構築するだけです。

使用後はmt-keywords2tags.cgiを削除しておくことをお忘れなく。

## See Also

## License

This code is released under the Artistic License. The terms of the Artistic License are described at [http://www.perl.com/language/misc/Artistic.html](http://www.perl.com/language/misc/Artistic.html).

## Author & Copyright

Copyright 2006, Hirotaka Ogawa (hirotaka.ogawa at gmail.com)
