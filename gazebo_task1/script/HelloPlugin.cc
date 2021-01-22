#include <gazebo/gazebo.hh>
namespace gazebo
{
	class HelloPlugin : public WorldPlugin
	{
		public:
			HelloPlugin():WorldPlugin(){
				std::cout<<"\n\nHello GAZEBO\n\n";
			}
			void Load(physics::WorldPtr _world,sdf::ElementPtr _sdf){
			}
	};
	GZ_REGISTER_WORLD_PLUGIN(HelloPlugin)
}
