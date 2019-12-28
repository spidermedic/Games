class Colors():
    """ANSI ESC code for terminal colors"""

    def __init__(self):
        
        # Font colors
        self.blk = "\x1B[30m"
        self.red = "\x1B[31m"
        self.grn = "\x1B[32m"
        self.yel = "\x1B[33m"
        self.blu = "\x1B[34m"
        self.mag = "\x1B[35m"
        self.cya = "\x1B[36m"
        self.wht = "\x1B[37m"

        # Background colors
        self.blkbg = "\x1B[40m"
        self.whtbg = "\x1B[47m"

        # Atributes
        self.rev = "\x1B[7m"
        self.norm = "\x1B[0m"
