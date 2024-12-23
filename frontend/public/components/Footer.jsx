import React from 'react';
import { Button } from '@/components/ui/button';
import { Github } from 'lucide-react';

const Footer = () => (
  <footer className="bg-white border-t">
    <div className="max-w-7xl mx-auto px-4 py-6">
      <div className="flex flex-col md:flex-row justify-between items-center">
        <div className="flex items-center space-x-4">
          <img
            src="/api/placeholder/32/32"
            alt="Collabo"
            className="h-8"
          />
          <a
            href="https://github.com/Yermehyaw/collabo-app"
            className="text-gray-600 hover:text-gray-900 transition-colors"
            target="_blank"
            rel="noopener noreferrer"
          >
            <Github className="w-5 h-5" />
          </a>
        </div>
        <div className="flex space-x-6 mt-4 md:mt-0 text-sm">
          <Button
            variant="link"
            className="text-gray-600 hover:text-gray-900 p-0 h-auto"
          >
            FAQ
          </Button>
          <Button
            variant="link"
            className="text-gray-600 hover:text-gray-900 p-0 h-auto"
          >
            Terms of Use
          </Button>
          <Button
            variant="link"
            className="text-gray-600 hover:text-gray-900 p-0 h-auto"
          >
            Our Team
          </Button>
        </div>
      </div>
    </div>
  </footer>
);

export default Footer;
