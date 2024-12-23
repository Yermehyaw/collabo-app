import React from "react";
import FeatureCard from "./FeatureCard";
import { Zap, MessageSquare, Users } from "lucide-react";

interface FeatureGridProps {
  features?: Array<{
    icon: React.ComponentType<React.SVGProps<SVGSVGElement>>;
    title: string;
    description: string;
  }>;
}

const FeatureGrid = ({ features }: FeatureGridProps) => {
  const defaultFeatures = [
    {
      icon: MessageSquare,
      title: "Real-time Collaboration",
      description:
        "Work together seamlessly with your team in real-time with instant updates and notifications.",
    },
    {
      icon: Zap,
      title: "Lightning Fast",
      description:
        "Experience blazing fast performance with our optimized platform built for speed.",
    },
    {
      icon: Users,
      title: "Team Management",
      description:
        "Easily manage your team members, roles, and permissions in one central location.",
    },
  ];

  const displayFeatures = features || defaultFeatures;

  return (
    <section className="py-24 px-4 bg-gray-50">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-16">
          <h2 className="text-3xl font-bold text-gray-900 sm:text-4xl mb-4">
            Powerful Features
          </h2>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Discover the tools that will transform the way your team works
            together.
          </p>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {displayFeatures.map((feature, index) => (
            <FeatureCard
              key={index}
              icon={feature.icon}
              title={feature.title}
              description={feature.description}
            />
          ))}
        </div>
      </div>
    </section>
  );
};

export default FeatureGrid;
