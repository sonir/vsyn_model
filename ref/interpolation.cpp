
	#include "Interpolation.h"

	Interpolation::Interpolation(){

		step_count = 0;
        random_scale = 0.3;

	}

	void Interpolation::init(float got_st, float got_ed, int got_step){

		st = got_st;
		ed = got_ed;
		step = got_step;
        step_count = 0;

	}

	float Interpolation::update(){

		if(step_count>=step) return now;

		step_count++;
		now = st + ( ((ed-st)/step) * step_count );
		return now;

	}
