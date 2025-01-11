import React from 'react';
import { Button } from '@/components/ui/button';
import { ArrowRight } from 'lucide-react';

const HeroSection = ({
  headline = "Transform Your Team Collaboration",
  subheading = "Empower your team with our intuitive collaboration platform. Get more done together, faster and smarter.",
  ctaText = "Get Started",
  onCtaClick = () => console.log("CTA clicked")
}) => {
  return (
    <section className="min-h-[600px] w-full bg-white flex items-center justify-center px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto text-center space-y-8 animate-fade-in">
        <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-gray-900 tracking-tight">
          {headline}
        </h1>
        <p className="text-xl sm:text-2xl text-gray-600 max-w-2xl mx-auto">
          {subheading}
        </p>
        <div className="pt-4">
          <Button
            size="lg"
            onClick={onCtaClick}
            className="group hover:scale-105 transition-transform duration-200"
          >
            {ctaText}
            <ArrowRight className="ml-2 h-4 w-4 group-hover:translate-x-1 transition-transform duration-200" />
          </Button>
        </div>
        <div className="pt-12">
          <img
            src="/api/placeholder/800/400"
            alt="Team collaboration"
            className="rounded-lg shadow-2xl mx-auto max-w-full"
            width={800}
            height={400}
          />
        </div>
      </div>
    </section>
  );
};

export default HeroSection;
