"use client";

import Button from "@/components/button";

export default function Home() {
    return (
        <main className="flex min-h-screen flex-col items-center p-24 gap-4">
            <h1>React Counter Button</h1>
            <Button />
            <Button />
        </main>
    );
}