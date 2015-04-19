title: Git study notes
slug: git-study-notes
date: 2015-04-18
tags: [git]
published: 2015-04-18
summary: Some notes on git I have collected through the years.
public: yes

Git Merge VS Rebase

http://blogs.atlassian.com/2013/10/git-team-workflows-merge-or-rebase/
    If you and your team are not familiar with, or don’t understand the intricacies of rebase, then you probably shouldn’t use it. In this context, always merge is the safest option.
    If you and your team are familiar with both options, then the main decision revolves around this: Do you value more a clean, linear history? Or the traceability of your branches? In the first case go for a rebase policy, in the later go for a merge one.
    Note that a rebase policy comes with small contraindications and takes more effort.
    Case: Atlassian
        The policy is always to merge feature branches, and require that branches are merged through a pull request for quality and code review. But the team is not too strict around fast-forward.

http://www.arruda.blog.br/programacao/dicas-de-git-rebase-vs-merge/
    Nesse post no final ele manda usar o rebase no momento do pull, e jamais no push.


---

### CONSIDERATIONS ###

Fork this repository on github: https://github.com/developer/awesomeproject.

The idea is that we will work on this forked repository and then make pull requests to the developer/awesomeproject repository master branch.

Your forked repository remote is called "remote origin", and the developer official repository remote is called "remote awesomeproject".

### Workflow ###

On your repository (remote origin) you can do whatever you want and even work on your separate branches. After finishing up, you must consolidate all of your changes into your master branch.

After that, you must make a pull request on Github to developer/awesomeproject. Your work will be reviewed and then rebased into developer/awesomeproject master branch, which then will be ready to be deployed on production.

To get the master branch from your local fork:

```
        $ git pull origin master
```

To get the master branch from the official developer/awesomeproject:

```
        $ git fetch awesomeproject
        $ git rebase awesomeproject/master
        $ git pull
```

NOTE:
    - Se der algum problema / conflito durante o rebase, corrigir - fazendo os respectivos git add e/ou editando os arquivos. Depois de pronto:
        $ git rebase --continue
        (continuar fazendo esse "rebase --continue" e corrigindo até resolver todos os conflitos)

    - Depois de terminar o rebase com sucesso:
        $ git push origin master

        Se der algum conflito:
            - fazer novamente o git pull:
                $ git pull origin master

            - fazer as correcões necessárias e commitar:
                    $ git commit

            - fazer outro git pull:
                    $ git pull origin master

            - fazer o push:
                    $ git push origin master

- Após o término, é só fazer o pull request do meu fork para o projeto original.


Your git config file (found on the project root, under ".git/config") must be like below - just change "tiagoprn" to your Github's account name:

```
[core]
    repositoryformatversion = 0
    fileMode = false
    bare = false
    logallrefupdates = true
[remote "origin"]
    url = https://github.com/tiagoprn/awesomeproject.git
    fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
    remote = origin
    merge = refs/heads/master
[remote "awesomeproject"]
    url = https://github.com/developer/awesomeproject.git
    fetch = +refs/heads/*:refs/remotes/awesomeproject/*
```
### Referencies ###
* http://robots.thoughtbot.com/keeping-a-github-fork-updated

