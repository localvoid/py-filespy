((python-mode . ((eval . (setq compile-command (concat "make -C " (locate-dominating-file buffer-file-name ".dir-locals.el") " check"))))))
