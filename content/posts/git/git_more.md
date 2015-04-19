title: Git cheatsheet
slug: git-cheatsheet
date: 2015-04-18
tags: [git]
published: 2015-04-08
summary: Many practical git notes.
public: yes

Git:

- Logs:
    Most recent (last one):
        $ git log -1
    3 Most recents (3 last ones):
        $ git log -3

- Clones a remote branch (cool_repository/master) to a local branch of yours (remote_master):
    $ git checkout -B remote_master cool_repository/master --no-track

- Deletes a branch (locally):
    $ git branch -D nome_da_branch

- Temporarily change a branch to a prior commit hash:
    git reset --hard fd19da2dce866607118db92c753e922ff5108ec6

- Keeping a fork of yours updated:
    Example:
        original repo: othergituser/cool_repository
        fork repo: tiagoprn/cool_repository

    1) Add a remote pointing to the original repository (if you didn't already):
        $ git remote add upstream git@github.com:othergituser/cool_repository.git

    2) Update to your local master branch, if you're not on it already:
        $ git checkout master

    3) Fetch / Rebase:
        $ git fetch upstream
        $ git rebase upstream/master

    4) Check the status:
        $ gitk
        Your local master and upstream/master should be on the same baseline.
        If your origin/master is below both:
            $ git push origin master


- How to configure "alias" for git commands:
    $ git config alias.br "symbolic-ref --short HEAD"
    $ git config alias.hist "log -10 --pretty=format:'%h %ad | %s%d [%an]' --graph --"

    To use:
        $ git br
        $ git hist


- Git global configuration (for the user):

    $ vim ~/.gitconfig
        [user]
            email = tiagoprn@gmail.com
            name = tiagoprn
        [diff]
            external = git-meld
        [merge]
            tool = meld

    In the example above, I'm also setting "meld" as my diff tool.
    "git-meld" must be a shell script like:
        $ touch /usr/bin/git-meld
        $ chmod 766 /usr/bin/git-meld
        $ vim /usr/bin/git-meld
            #!/bin/bash
            meld "$2" "$5"

- Fluxo de atualizar meu branch com as mudanças do master:
    $ git checkout master (vou para o master)
    $ git pull origin master (atualizo meu master)
    $ git checkout pneustore_spider (volto para o meu branch)
    $ git rebase master (atualizo meu branch com as mudanças do master)
