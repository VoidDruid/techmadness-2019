package com.avaskov.techmadness.domain.executor;

import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

public class ThreadExecutor implements Executor {

    private static final int CORE_POOL_SIZE = 3;
    private static final int MAX_POOL_SIZE = 5;
    private static final long KEEP_ALIVE_TIME = 120;
    private static final TimeUnit TIME_UNIT = TimeUnit.SECONDS;
    private static final BlockingQueue<Runnable> WORK_QUEUE = new LinkedBlockingQueue<Runnable>();
    private static volatile ThreadExecutor threadExecutor;
    private ThreadPoolExecutor threadPoolExecutor;

    private ThreadExecutor() {
        threadPoolExecutor = new ThreadPoolExecutor(
                CORE_POOL_SIZE,
                MAX_POOL_SIZE,
                KEEP_ALIVE_TIME,
                TIME_UNIT,
                WORK_QUEUE);
    }

    public static Executor getInstance() {
        if (threadExecutor == null) {
            threadExecutor = new ThreadExecutor();
        }

        return threadExecutor;
    }

    @Override
    public void execute(Runnable runnable) {
        threadPoolExecutor.submit(runnable);
    }
}
