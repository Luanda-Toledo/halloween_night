from enemy import Enemy
from auxiliar import Auxiliar


class EnemyEsqueletin(Enemy):

    def __init__(self, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100) -> None:
        
        super().__init__(x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100)
        
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/esquelin/esqueletin.png", 0, 1, scale = p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/esquelin/esqueletin.png", 0, 1, flip = True, scale = p_scale)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/esquelin/esqueletin.png", 0, 1, scale = p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/esquelin/esqueletin.png", 0, 1, flip = True, scale = p_scale)


class EnemyZombie(Enemy):

    def __init__(self, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100) -> None:
        
        super().__init__(x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100)
        
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/Archive(1)/walk/go_5.png", 0, 1, scale = 0.08)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/Archive(1)/idle/idle_2.png", 0, 1, flip = True, scale = 0.08)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/Archive(1)/attack/hit_2.png", 0, 1, scale = 0.08)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/Archive(1)/attack/hit_7.png", 0, 1, flip = True, scale = 0.08)


class EnemyFantasmin(Enemy):

    def __init__(self, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100) -> None:
        
        super().__init__(x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100)
        
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/fantasmin/fantasmin_der.png", 0, 1, scale = 0.05)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/fantasmin/fantasmin_der.png", 0, 1, flip = True, scale = 0.05)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/fantasmin/fantasmin_frent.png", 0, 1, scale = 0.05)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/fantasmin/fastasmin_izqq.png", 0, 1, flip = True, scale = 0.05)


class EnemyMurcielago(Enemy):

    def __init__(self, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100) -> None:
        
        super().__init__(x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100)
        
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/murcielg.png", 1, 5, scale = 0.02)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/murcielg.png", 2, 5, flip = True, scale = 0.02)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/murcielg.png", 3, 5, scale = 0.02)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/murcielg.png", 3, 5, flip = True, scale = 0.02)


class EnemyVampiro(Enemy):

    def __init__(self, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100) -> None:
        
        super().__init__(x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100)
        
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/Archive/attack/hit_6.png", 0, 1, scale = 0.08)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/Archive/attack/hit_13.png", 0, 1, flip = True, scale = 0.08)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/Archive/attack/hit_1.png", 0, 1, scale = 0.08)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/Archive/attack/hit_11.png", 0, 1, flip = True, scale = 0.08)


class EnemyEqueco(Enemy):

    def __init__(self, x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100) -> None:
        
        super().__init__(x, y, speed_walk, speed_run, gravity, jump_power, frame_rate_ms, move_rate_ms, jump_height, 
                 p_scale = 1, interval_time_jump = 100)
        
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/prin.png", 0, 1, scale = 0.04)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/prin.png", 0, 1, flip = True, scale = 0.04)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/prin.png", 0, 1, scale = 0.04)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("recursos/enemigos/prin.png", 0, 1, flip = True, scale = 0.04)












