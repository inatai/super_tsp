# githubでチーム開発をする流れ  

[参考][https://www.flock.codes/Wqu2Rh22633p4dFdnG3E]

## はじめに 

作業したいディレクトリで  
`git clone https://github.com/inatai/super_tsp.git`  
を実行し、自分のリモート環境に*main*を作成する。  
　  
　  


## 作業の流れ

1. `git pull origin master`  で「ローカルのmain」を「リモートのmain」と同じ状態にする
2. vscodeフッター左の「main」→「新しいブランチを作る」クリック  
3. 変更予定の内容などがわかるような名前で、ローカルにブランチを作成(例:「feature/title」)  
  
 ローカルのブランチ内で作業後  
   
4. 作業内容がわかるコメントを添えてコミット  
5. ブランチを同期(push)をクリック  
6. github上で「compare & pull request」をクリック  
7. Reviewersを誰か承認してほしい人に設定、または設定しないまま  
8. Assigneesを自分のアカウントに設定  
9. 「create pull request」をクリック  
  
*承認する人*  

10. pull requestタブでチェックしたいrequestをクリックして確認  
11. 「Marge pull request」をクリック  
12. 「Delete branch」をクリック  

*承認された人*  

13. vscode上で[ctrl+shift+P]を押してbranch deleteを入力選択後、消去したいブランチをクリック  