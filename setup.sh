#! /bin/bash

# Install necessary programs
sudo dnf install util-linux-user zsh vim git

# Setup vim
mkdir vim/backup vim/swapfile vim/bundle
ln -s "$(pwd)/vim" ~/.vim
ln -s "$(pwd)/vim/vimrc" ~/.vimrc
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

# Setup zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
rm ~/.zshrc
ln -s "$(pwd)/zsh/zshrc" ~/.zshrc

# Link directory of bin files
ln -s "$(pwd)/bin" ~/bin
