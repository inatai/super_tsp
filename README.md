# githubでチーム開発をする流れ  

[参考][https://www.flock.codes/Wqu2Rh22633p4dFdnG3E]

## はじめに 

作業したいディレクトリで  
`git clone https://github.com/inatai/super_tsp.git`  
を実行し、自分のリモート環境に*main*を作成する。  
　  
　  


## 作業の流れ

1. vscodeフッター左の「main」→「新しいブランチを作る」クリック  
2. 変更予定の内容などがわかるような名前で、ローカルにブランチを作成(例:「feature/title」)  
  
 ローカルのブランチ内で作業後  
   
3. 作業内容がわかるコメントを添えてコミット  
4. ブランチを同期(push)をクリック  
5. github上で「compare & pull request」をクリック  
6. Reviewersを誰か承認してほしい人に設定、または設定しないまま  
7. Assigneesを自分のアカウントに設定  
8. 「create pull request」をクリック  
  
*承認する人*  

9. pull requestタブでチェックしたいrequestをクリックして確認  
10. 「Marge pull request」をクリック  
11. 「Delete branch」をクリック  

*承認された人*  

12. vscode上で[ctrl+shift+P]を押してbranch deleteを入力選択後、消去したいブランチをクリック  