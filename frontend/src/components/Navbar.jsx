import { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import { Activity, ShieldCheck, Home, LogIn, UserPlus, LayoutDashboard, LogOut, Menu, X } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

const Navbar = () => {
    const [scrolled, setScrolled] = useState(false);
    const [isOpen, setIsOpen] = useState(false);
    const location = useLocation();
    const { user, logout } = useAuth();

    useEffect(() => {
        const handleScroll = () => {
            setScrolled(window.scrollY > 20);
        };
        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    }, []);

    useEffect(() => {
        setIsOpen(false);
    }, [location]);

    const navLinks = user ? [
        { path: '/', label: 'Home', icon: Home },
        { path: '/dashboard', label: 'Dashboard', icon: LayoutDashboard },
    ] : [
        { path: '/', label: 'Home', icon: Home },
        { path: '/login', label: 'Login', icon: LogIn },
        { path: '/register', label: 'Register', icon: UserPlus },
    ];

    return (
        <nav
            className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${scrolled || isOpen ? 'py-4 bg-slate-900/80 backdrop-blur-md border-b border-white/10' : 'py-6 bg-transparent'
                }`}
        >
            <div className="container mx-auto px-6 flex justify-between items-center">
                <Link to="/" className="flex items-center gap-3 group">
                    <div className="relative">
                        <img 
                            src="/logo.png" 
                            alt="Logo" 
                            className="w-10 h-10 rounded-lg group-hover:shadow-[0_0_20px_rgba(34,211,238,0.5)] transition-all duration-300"
                        />
                        <div className="absolute inset-0 bg-cyan-400/20 blur-md rounded-lg opacity-0 group-hover:opacity-100 transition-opacity" />
                    </div>
                    <span className="text-xl md:text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-400 group-hover:from-cyan-400 group-hover:to-blue-400 transition-all duration-300">
                        FakeJob<span className="text-cyan-500">Detector</span>
                    </span>
                </Link>

                {/* Desktop Navigation */}
                <div className="hidden md:flex items-center gap-4">
                    <div className="flex items-center gap-2">
                        {navLinks.map((link) => {
                            const Icon = link.icon;
                            const isActive = location.pathname === link.path;
                            return (
                                <Link
                                    key={link.path}
                                    to={link.path}
                                    className={`relative flex items-center gap-2 px-4 py-2 rounded-full transition-all duration-300 ${isActive
                                        ? 'text-cyan-400 bg-white/10 shadow-[0_0_15px_rgba(34,211,238,0.3)]'
                                        : 'text-gray-400 hover:text-white hover:bg-white/5'
                                        }`}
                                >
                                    <Icon className="w-4 h-4" />
                                    <span className="font-medium">{link.label}</span>
                                    {isActive && (
                                        <motion.div
                                            layoutId="nav-glow"
                                            className="absolute inset-0 rounded-full bg-cyan-400/20 blur-sm -z-10"
                                            transition={{ type: 'spring', bounce: 0.2, duration: 0.6 }}
                                        />
                                    )}
                                </Link>
                            );
                        })}
                    </div>
                    {user && (
                        <button
                            onClick={logout}
                            className="flex items-center gap-2 px-4 py-2 rounded-full text-red-400 hover:text-red-300 hover:bg-red-500/10 transition-all duration-300"
                        >
                            <LogOut className="w-4 h-4" />
                            <span className="font-medium">Logout</span>
                        </button>
                    )}
                </div>

                {/* Mobile Menu Toggle */}
                <button 
                    className="md:hidden p-2 text-gray-400 hover:text-white transition-colors" // Changed lg:hidden to md:hidden
                    onClick={() => setIsOpen(!isOpen)}
                >
                    {isOpen ? <X className="w-8 h-8" /> : <Menu className="w-8 h-8" />} {/* Changed to X and Menu icons */}
                </button>
            </div>

            {/* Mobile Navigation Drawer */}
            <AnimatePresence>
                {isOpen && (
                    <motion.div
                        initial={{ opacity: 0, height: 0 }}
                        animate={{ opacity: 1, height: 'auto' }}
                        exit={{ opacity: 0, height: 0 }}
                        className="md:hidden bg-slate-900/95 backdrop-blur-xl border-b border-white/10 overflow-hidden" // Changed lg:hidden to md:hidden
                    >
                        <div className="container mx-auto px-6 py-8 flex flex-col gap-4">
                            {navLinks.map((link) => {
                                const Icon = link.icon;
                                const isActive = location.pathname === link.path;
                                return (
                                    <Link
                                        key={link.path}
                                        to={link.path}
                                        className={`flex items-center gap-4 px-6 py-4 rounded-xl transition-all ${isActive
                                            ? 'bg-cyan-500/10 text-cyan-400 border border-cyan-500/20'
                                            : 'text-gray-400 hover:bg-white/5'
                                            }`}
                                    >
                                        <Icon className="w-5 h-5" />
                                        <span className="text-lg font-medium">{link.label}</span>
                                    </Link>
                                );
                            })}
                            {user && (
                                <button
                                    onClick={logout}
                                    className="flex items-center gap-4 px-6 py-4 rounded-xl text-red-400 hover:bg-red-500/10 transition-all mt-4 border border-red-500/10"
                                >
                                    <LogOut className="w-5 h-5" />
                                    <span className="text-lg font-medium">Logout</span>
                                </button>
                            )}
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
        </nav>
    );
};

export default Navbar;
